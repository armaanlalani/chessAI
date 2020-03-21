from chessPlayer import *

board = genBoard() # implements the board structure for the game
printBoard(board)

while True: 
   pieces = GetPlayerPositions(board,10)
   print(pieces) # displays the pieces available to move
   legal = False
   while legal == False:
      player = int(input("WHITE: Select the piece you wish to move: "))
      for i in pieces:
         if player == i:
            legal = True
   moves = GetPieceLegalMoves(board,player) # displays the moves available for the chosen piece
   moves.sort()
   print(moves)
   legal = False
   while legal == False: # allows the user to choose the move they wish to make
      move = int(input("WHITE: Select the position you wish to move to: (Enter -1 to go back)"))
      if move == -1:
         break
      for i in moves:
         if move == i:
            legal = True
   while move == -1: # if the user wishes to go back
      pieces = GetPlayerPositions(board,10)
      print(pieces)
      legal = False
      while legal == False:
         player = int(input("WHITE: Select the piece you wish to move: "))
         for i in pieces:
            if player == i:
               legal = True
      moves = GetPieceLegalMoves(board,player)
      moves.sort()
      print(moves)
      legal = False
      while legal == False: # allows the user to choose the position they wish to move to
         move = int(input("WHITE: Select the position you wish to move to: (Enter -1 to go back)"))
         if move == -1:
            break
         for i in moves:
            if move == i:
               legal = True
   while legal == False:
      move = int(input("WHITE: Select the position you wish to move to: (Enter -1 to go back)"))
      for i in moves:
         if move == i or move == -1:
            legal = True
   b = list(board)
   Move(b,player,move)
   while check(b,10):
      move = int(input("You are in check, please try again")) # if the move the player makes puts them in or keeps them in the 'check' position, they are required to make another move
      b[player] = board[player]
      b[move] = board[move]
   Move(board,player,move)
   printBoard(board)
   if checkmate(board,20): # checks game ending condition
      print("WHITE WINS THE GAME")
      break

   opponent = chessPlayer(board,20) # instantiates the computer's move
   print(opponent[0:3])
   print("Opponent Move")
   print("From: " + str(opponent[1][0]))
   print("To: " + str(opponent[1][1]))
   print("queen: " + str(QueenMobility(board,opponent[1][0],opponent[1][1],20)))
   print("bishop: " + str(BishopMobility(board,opponent[1][0],opponent[1][1],20)))
   print("king: " + str(KingProtection(board,opponent[1][0],opponent[1][1],20)))
   print("kill: " + str(KillValue(board,opponent[1][0],opponent[1][1],20)))
   print("check: " + str(CheckValue(board,opponent[1][0],opponent[1][1],20)))
   print("checkmate: " + str(CheckMateValue(board,opponent[1][0],opponent[1][1],20)))
   print("protect: " + str(Protect(board,opponent[1][0],opponent[1][1],20)))
   print("inthreat: " + str(InThreat(board,opponent[1][0],opponent[1][1],20)))
   Move(board,int(opponent[1][0]),int(opponent[1][1])) # performs the best possible move available
   printBoard(board)
   if checkmate(board,10): # checks game ending condition
      print("BLACK WINS THE GAME")
      break
