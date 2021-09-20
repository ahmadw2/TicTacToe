import turtle
import time

# creates the screen
screen = turtle.Screen()
screen.tracer(0)
screen.title("Tic Tac Toe")
screen.bgcolor("CadetBlue1")

# turtle draws the board, Xs and Os
turtle.hideturtle()
turtle.pencolor("CadetBlue3")
turtle.pensize(9)

# messenger relays messages to user they win or lose
messenger = turtle.Turtle()
messenger.hideturtle()
messenger.penup()
messenger.goto(0, 170)
messenger.color("CadetBlue4")


# creates the Tic Tac Toe board
def draw_board():

    turtle.penup()
    turtle.goto(-50, 150)
    turtle.pendown()
    turtle.goto(-50, -150)

    turtle.penup()
    turtle.goto(50, 150)
    turtle.pendown()
    turtle.goto(50, -150)

    turtle.penup()
    turtle.goto(-150, 50)
    turtle.pendown()
    turtle.goto(150, 50)

    turtle.penup()
    turtle.goto(-150, -50)
    turtle.pendown()
    turtle.goto(150, -50)

    screen.update()


# draws an X in the designated square
def drawX(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pencolor("azure4")
    turtle.pendown()
    turtle.seth(45)

    for i in range(2):
        turtle.forward(40)
        turtle.backward(80)
        turtle.forward(40)
        turtle.left(90)

    screen.update()

# draws an O in the designated square
def drawO(x, y):
  turtle.penup()
  turtle.goto(x-20, y+20)
  turtle.pencolor("azure1")
  turtle.pendown()
  turtle.circle(30)
  screen.update()


# adds an X to the 2D list
def addX(row, column):
  messenger.clear()
  if board[row][column] == "X" or board[row][column] == "O":
    messenger.write("That square is already filled!", align="center", font=("Arial", 14, "bold"))
    screen.update()
  else:
    drawX(-100 + 100 * column, 100 - 100 * row)
    board[row][column] = "X"

    if checkWinner("X"):
      messenger.write("You Win!", align="center", font = ("Arial", 15, "bold"))
      screen.update()
    else:
      time.sleep(1)
      addO()
      if checkWinner("O"):
        messenger.write("You Lose!", align="center", font = ("Arial", 15, "bold"))
        screen.update()
      elif checkDraw():
        messenger.write("It's a tie!", align="center",font = ("Arial", 15, "bold"))
        screen.update()


# adds an O to the 2D list (computer plays O)
def addO():
  # checks to see if it can win three in a row
  for i in range(3):
    for j in range(3):
      if board[i][j] == " ":
        board[i][j] = "O"
        if checkWinner("O"):
          drawO(-100 + 100 * j, 100 - 100 * i)
          return
        board[i][j] = " "

  # checks to see if it can block player
  for i in range(3):
    for j in range(3):
      if board[i][j] == " ":
        board[i][j] = "X"
        if checkWinner("X"):
          board[i][j] = "O"
          drawO(-100 + 100 * j, 100 - 100 * i)
          return
        board[i][j] = " "

  # Try to place O in a corner
  for i in range(0, 3, 2):
    for j in range(0, 3, 2):
      if board[i][j] == " ":
        board[i][j] = "O"
        drawO(-100 + 100 * j, 100 - 100 * i)
        return

  # In case the other three don't place O
  for i in range(3):
    for j in range(3):
      if board[i][j] == " ":
        board[i][j] = "O"
        drawO(-100 + 100 * j, 100 - 100 * i)
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


# functions for each square
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

# has the square coordinates to track user's clicks
def button_click(x, y):
  if -150 <= x <= -50:
    if 50 < y <= 150:
      squareOne()
      return
    if -50 <= y <= 50:
      squareFour()
      return
    if -150 <= y < -50:
      squareSeven()
      return
  if -50 < x <= 50:
    if 50 < y <= 150:
      squareTwo()
      return
    if -50 <= y <= 50:
      squareFive() 
      return
    if -150 <= y < -50:
      squareEight() 
      return
  if 50 < x <= 150:
    if 50 < y <= 150:
      squareThree()
      return
    if -50 <= y <= 50:
      squareSix() 
      return
    if -150 <= y < -50:
      squareNine() 
      return

    
# draws the tic tac toe board
draw_board()

# creates the 2D list to store the X and O values
board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(" ")
    board.append(row)

# allows user to click on screen to place their Xs
screen.onclick(button_click)

# waits for user to close the screen
turtle.done()
