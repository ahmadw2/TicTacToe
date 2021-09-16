import turtle
import time

# creates the screen
screen = turtle.Screen()
screen.tracer(0)
screen.title("Tic Tac Toe")
screen.bgcolor("black")

# turtle draws the board, Xs and Os
turtle.hideturtle()
turtle.pencolor("white")
turtle.pensize(4)

# messenger relays messages to user they win or lose
messenger = turtle.Turtle()
messenger.hideturtle()
messenger.penup()
messenger.goto(-90, 107)
messenger.color("red")


# creates the Tic Tac Toe board
def draw_board():
    # vertical lines
    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pendown()
    turtle.goto(-100, -100)

    turtle.penup()
    turtle.goto(-33.3, 100)
    turtle.pendown()
    turtle.goto(-33.3, -100)

    turtle.penup()
    turtle.goto(33, 100)
    turtle.pendown()
    turtle.goto(33, -100)

    turtle.penup()
    turtle.goto(100, 100)
    turtle.pendown()
    turtle.goto(100, -100)

    # horizontal lines
    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pendown()
    turtle.goto(100, 100)

    turtle.penup()
    turtle.goto(-100, 33.3)
    turtle.pendown()
    turtle.goto(100, 33.3)

    turtle.penup()
    turtle.goto(-100, -33.3)
    turtle.pendown()
    turtle.goto(100, -33.3)

    turtle.penup()
    turtle.goto(-100, -100)
    turtle.pendown()
    turtle.goto(100, -100)

    num = 1
    for i in range(3):
        for j in range(3):
            turtle.penup()
            turtle.goto(-92 + j * 66, 83 - i * 66)
            turtle.write(num, font=('Arial', 7))
            num += 1


# draws an X in the designated square
def drawX(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pensize(2)
    turtle.pendown()
    turtle.seth(45)

    for i in range(2):
        turtle.forward(20)
        turtle.backward(40)
        turtle.forward(20)
        turtle.left(90)

    screen.update()

# checks if there's a tie
def checkDraw():
  count = 0
  for i in range(3):
    for j in range(3):
      if board[i][j] == "X":
        count += 1

  if count > 3:
    return True
  else:
    return False

# draws an O in the designated square
def drawO(x, y):
  turtle.penup()
  turtle.goto(x-15, y+15)
  turtle.pendown()
  turtle.circle(20)
  screen.update()


# adds an X to the 2D list
def addX(row, column):
  messenger.clear()
  if board[row][column] == "X" or board[row][column] == "O":
    messenger.write("That square is already filled!", font=("Arial", 10))
    screen.update()
  else:
    drawX(-66 + 66 * column, 66 - 66 * row)
    board[row][column] = "X"

    if checkWinner("X"):
      messenger.goto(-50, 107)
      messenger.color("green")
      messenger.write("You Win!", font = ("Arial", 15))
      screen.update()  
    else:
      time.sleep(1)
      addO()
      if checkWinner("O"):
        messenger.goto(-50, 107)
        messenger.color("red")
        messenger.write("You Lost!", font = ("Arial", 15))
        screen.update()
      elif checkDraw():
        messenger.goto(-40, 107)
        messenger.color("cyan")
        messenger.write("It's a tie!", font = ("Arial", 15))
        screen.update()


# adds an O to the 2D list (computer plays O)
def addO():
  # checks to see if it can win three in a row
  for i in range(3):
    for j in range(3):
      if board[i][j] == " ":
        board[i][j] = "O"
        if checkWinner("O"):
          drawO(-66 + 66 * j, 66 - 66 * i)
          return
        board[i][j] = " "

  # checks to see if it can block player
  for i in range(3):
    for j in range(3):
      if board[i][j] == " ":
        board[i][j] = "X"
        if checkWinner("X"):
          board[i][j] = "O"
          drawO(-66 + 66 * j, 66 - 66 * i)
          return
        board[i][j] = " "

  # Try to place O in a corner
  for i in range(0, 3, 2):
    for j in range(0, 3, 2):
      if board[i][j] == " ":
        board[i][j] = "O"
        drawO(-66 + 66 * j, 66 - 66 * i)
        return

  # In case the other three don't place O
  for i in range(3):
    for j in range(3):
      if board[i][j] == " ":
        board[i][j] = "O"
        drawO(-66 + 66 * j, 66 - 66 * i)
        return
      

# checks if X or O has three in a row
def checkWinner(letter):
  # check rows
  for i in range(3):
    if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == letter:
      return True

  # check columns
  for i in range(3):
    if board[0][i] == board[1][i] and board[1][i] and board[1][i] == board[2][i] and board[0][i] == letter:
      return True

  # check diagonals
  for i in range(3):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == letter:
      return True
  
  for i in range(3):
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board [0][2] == letter:
      return True
  return False

# functions for calling each square
def squareOne():
  addX(0, 0)
def squareTwo():
  addX(0, 1)
def squareThree():
  addX(0, 2)
def squareFour():
  addX(1, 0)
def squareFive():
  addX(1, 1)
def squareSix():
  addX(1, 2)
def squareSeven():
  addX(2, 0)
def squareEight():
  addX(2, 1)
def squareNine():
  addX(2, 2)

# list of functions
functions = [squareOne, squareTwo, squareThree, squareFour, squareFive, squareSix, squareSeven, squareEight, squareNine]

# draws the tic tac toe board
draw_board()

# creates the 2D list to store the X and O values
board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(" ")
    board.append(row)

while not checkDraw() and not checkWinner("O") and not checkWinner("X"):
  value = int(input("Which square do you want to place your X in? "))
  functions[value-1]()

# shows end screen for ten seconds before closing program
time.sleep(10)
