# must install xming server
# export DISPLAY=:0 to run gui for ubuntu terminal in windows 10

import turtle as t
import math
import random

# size is for horizontal lines and ratio is for vertical lines
size = 300
ratio = 100

# array to keep track of where pieces are placed
board = ['', '', '', '', '', '', '', '', '']

# possible winning combos
combos = [[0, 1, 2],
          [3, 4, 5],
          [6, 7, 8], 
          [0, 3, 6], 
          [1, 4, 7], 
          [2, 5, 8],
          [0, 4, 8], 
          [2, 4, 6] ]  

# draws tic tac toe board
def drawBoard():
   t.hideturtle()

   # draw first horizontal
   t.penup()
   t.setpos(-size, ratio)
   t.pendown()
   t.forward(abs(t.xcor()) * 2)
   t.penup()

   # draw second horizontal
   t.setpos(-size, -ratio)
   t.pendown()
   t.forward(abs(t.xcor()) * 2)
   t.penup()

   # draw first vertical
   t.setpos(-ratio, size)
   t.pendown()
   t.right(90)
   t.forward(t.ycor() * 2)
   t.penup()

   # draw second vertical
   t.setpos(ratio, size)
   t.pendown()
   t.forward(t.ycor() * 2)
   t.penup()

   return

# draws an X
def makeX(a, b, c, d):
   t.setpos(a, b)
   t.right(45)
   t.pendown()
   t.forward((ratio-10) * 2.9)
   t.penup()

   t.setpos(c, d)
   t.right(90)
   t.pendown()
   t.forward((ratio-10) * 2.9)

   return

# draws an O
def makeO(a, b):   
   t.setpos(a, b)
   t.pendown()
   t.circle(ratio-10)
   return

def draw(index, player):

   # resets turtle position and orientation
   t.home()
   
   # X's start at the top right and left of each square
   # O's start at the bottom center of each square
   # 10 is used as offset for visual effect to show space between
   # board markings and play markings 

   if index == 0:
      if player == 'X':
         makeX(10-size, size-10, -ratio-10, size-10)

      elif player == 'O':
         makeO(ratio-size, ratio+10)

   elif index == 1:
      if player == 'X':
         makeX(10-ratio, size-10, ratio-10, size-10)

      elif player == 'O':
         makeO(0, ratio+10)

   elif index == 2:
      if player == 'X':
         makeX(ratio+10, size-10, size-10, size-10)

      elif player == 'O':
         makeO(size-ratio, ratio+10)

   elif index == 3:
      if player == 'X':
         makeX(10-size, ratio-10, -ratio-10, ratio-10)

      elif player == 'O':
         makeO(ratio-size, 10-ratio)

   elif index == 4:
      if player == 'X':
         makeX(10-ratio, ratio-10, ratio-10, ratio-10)

      elif player == 'O':
         makeO(0, 10-ratio)

   elif index == 5:
      if player == 'X':
         makeX(ratio+10, ratio-10, size-10, ratio-10)

      elif player == 'O':
         makeO(size-ratio, 10-ratio)

   elif index == 6:
      if player == 'X':
         makeX(10-size, -ratio-10, -ratio-10, -ratio-10)

      elif player == 'O':
         makeO(ratio-size, 10-size)
   
   elif index == 7:
      if player == 'X':
         makeX(-ratio+10, -ratio-10, ratio-10, -ratio-10)

      elif player == 'O':
         makeO(0, 10-size)
   
   elif index == 8:
      if player == 'X':
         makeX(ratio+10, -ratio-10, size-10, -ratio-10)

      elif player == 'O':
         makeO(size-ratio, 10-size)

   t.penup()
   t.home()
   return

# checks if board contains winning combos
def findWinner():
   for combo in combos:
      a = combo[0]
      b = combo[1]
      c = combo[2]

      if board[a] != '':
         if board[a] == board[b] and board[a] == board[c]:
            return combo

   return 0

# have to set pos to draw line for each combo
def drawLine(combo):
   # makes color red
   t.pencolor(255, 0, 0)

   # checks horizontal win
   if combo == combos[0]:
      t.setpos(-size, size-ratio)
      
   elif combo == combos[1]:
      t.setpos(-size, 0)

   elif combo == combos[2]:
      t.setpos(-size, ratio-size)

   # checks vertical win
   elif combo == combos[3]:
      t.setpos(ratio-size, size)
      t.right(90)

   elif combo == combos[4]:
      t.setpos(0, size)
      t.right(90)
      
   elif combo == combos[5]:
      t.setpos(size-ratio, size)
      t.right(90)

   # checks diagonal win
   elif combo == combos[6]:
      t.setpos(-size, size)
      t.right(45)
   
   elif combo == combos[7]:
      t.setpos(size, size)
      t.right(135)

   t.pendown()

   # diagonal lines are longer 
   if combo == combos[6] or combo == combos[7]:

      # pythagorean theorem to draw line for digaonal
      t.forward(math.sqrt((600**2) * 2))

   else:
      t.forward(size*2)

   t.penup()
   t.home()
   return

def tictactoe(moves, p1, p2):
   turn = 1

   # loop goes through each move in array
   for play in moves:

      # draw x
      if turn == 1:
         t.pencolor(0, 255, 150)
         draw(play, p1)
         board[play] = 'X'

      # draw o
      elif turn == 0:
         t.pencolor(100, 0, 255)
         draw(play, p2)
         board[play] = 'O'

      # change turn
      turn = (turn + 1) % 2

      # check board if a winner
      win = findWinner()
      
      # draw line through winning combo
      if win:
         drawLine(win)
         return

   return

def setup():

   # set colormode to 255 instead of 1.0
   t.colormode(255)

   # title for turtle gui window
   t.title('Tic Tac Toe')

   # speed up drawing the board
   t.speed(0)
   drawBoard()

   # return turtle to normal speed
   t.speed(6)

   # array of moves and shuffles for randomness
   moves = [x for x in range(9)]
   random.shuffle(moves)
   random.shuffle(moves)

   # function plays game of tic tac toe
   tictactoe(moves, 'X', 'O')

   return

def main():
   choice = 1
   title = 'Play Again?'
   prompt = 'Press 0 to quit or press 1 to play again'

   # set up window size
   t.setup(800, 800)

   while choice != 0:

      # sets up paramters for tic tac toe
      setup()

      # user input: 1 to play again 0 to quit
      choice = t.numinput(title, prompt, None, 0, 1)
      if choice == 1:
         # reset board
         for i in range(9):
            board[i] = ''

         # reset turtle drawings
         t.reset()

   # close turtle gui
   t.bye()
   return

if __name__ == '__main__':
   main()