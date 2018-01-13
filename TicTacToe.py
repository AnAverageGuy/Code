board = [[7,8,9],[4,5,6],[1,2,3]]
currentPlayer = 1


def newGame():
  global board
  board = [[0,0,0],[0,0,0],[0,0,0]]
  print("Spaces correspond to numbers on num pad.\n")
	
def printBoard():
  print(board[0])
  print(board[1])
  print(board[2])

def theresAWinner(player):
  if ((board[0][0] == player) and (board[0][1] == player) and (board[0][2] == player)) or ((board[1][0] == player) and (board[1][1] == player) and (board[1][2] == player)) or ((board[2][0] == player) and (board[2][1] == player) and (board[2][2] == player)) or ((board[0][0] == player) and (board[1][1] == player) and (board[2][2] == player)) or ((board[0][2] == player) and (board[1][1] == player) and (board[2][0] == player)) or ((board[0][0] == player) and (board[1][0] == player) and (board[2][0] == player)) or ((board[0][1] == player) and (board[1][1] == player) and (board[2][1] == player)) or ((board[0][2] == player) and (board[1][2] == player) and (board[2][2] == player)):
    print("Player ", player, " has won!")
    return True
  else:
    return False
			
def playerMove(boardR, boardC, player):
  board[boardR][boardC] = player

def markBoard(square, player):
  if ((square is 7) and (board[0][0] is 0)):#((space is "TL")
    playerMove(0,0,player)
  elif ((square is 8) and (board[0][1] is 0)):
    playerMove(0,1,player)
  elif ((square is 9) and (board[0][2] is 0)):
    playerMove(0,2,player)
  elif ((square is 4) and (board[1][0] is 0)):
    playerMove(1,0,player)
  elif ((square is 5) and (board[1][1] is 0)):
    playerMove(1,1,player)
  elif ((square is 6) and (board[1][2] is 0)):
    playerMove(1,2,player)
  elif ((square is 1) and (board[2][0] is 0)):
    playerMove(2,0,player)
  elif ((square is 2) and (board[2][1] is 0)):
    playerMove(2,1,player)  
  elif ((square is 3) and (board[2][2] is 0)):
    playerMove(2,2,player)  
	
def executePlayerTurn(player):
  print("Player", player)
  while True:
    try:
      square = int(input("Please select a space.\n>"))
    except ValueError:
      print("Invalid input.")
      continue
    
    if square < 0:
      print("Please select a real spot.")
      continue
    else:
      break
    
  print()
  markBoard(square, player)
   
  printBoard()
  
  if theresAWinner(player):
    return
  
  if player is 1:
    executePlayerTurn(2)
  else:
    executePlayerTurn(1)
	
def startGame():
	printBoard()
	newGame()
	executePlayerTurn(1)
	


startGame()