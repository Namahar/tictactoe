# must install xming server
# export DISPLAY=:0 to run gui for ubuntu terminal in windows 10

import turtle as t
import math

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
          [2, 4, 6] 
         ]  

scores = {
   'X': 1,
   'O': -1,
   'tie': 0
}

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
def find_winner():
   for combo in combos:
      a = combo[0]
      b = combo[1]
      c = combo[2]

      if board[a] != '':
         if board[a] == board[b] and board[a] == board[c]:
            return combo, board[a]

   if '' in board:
      return None, None
   else:
      return None, 'tie'

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

# if ismaximizing is true
# player is x
def minimax(depth, ismaximizing, alpha, beta):
   result, player = find_winner()
   if player != None:
      return scores[player]

   if ismaximizing:
      best_score = -math.inf
      for i in range(9):
         if board[i] == '':
            board[i] = 'X'
            score = minimax(depth + 1, False, alpha, beta)
            board[i] = ''
            best_score = max(score, best_score)

            alpha = max(score, alpha)
            if beta <= alpha:
               return best_score

      return best_score

   else:
      best_score = math.inf
      for i in range(9):
         if board[i] == '':
            board[i] = 'O'
            score = minimax(depth + 1, True, alpha, beta)
            board[i] = ''
            best_score = min(score, best_score)

            beta = min(beta, score)
            if beta <= alpha:
               return best_score

      return best_score

def best_move(turn):
   if turn:
      best_score = -math.inf
   else:
      best_score = math.inf

   move = math.inf

   for i in range(9):
      if board[i] == '':

         if turn:
            board[i] = 'X'
            score = minimax(0, False, -math.inf, math.inf)
            board[i] = ''
            if score > best_score:
               best_score = score
               move = i

         else:
            board[i] = 'O'
            score = minimax(0, True, -math.inf, math.inf)
            board[i] = ''
            if score < best_score:
               best_score = score
               move = i

   return move

def tictactoe(p1, p2):
   turn = 1

   # loop goes through each move in array
   for i in range(9):
      play = best_move(turn)

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
      win, player = find_winner()
      
      # draw line through winning combo
      if win != 'tie' and win != None:
         print(win)
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

   # function plays game of tic tac toe
   tictactoe('X', 'O')

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