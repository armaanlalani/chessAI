from chessPlayer import *

board = genBoard()
printBoard(board)

while True:
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
   while legal == False:
      move = int(input("WHITE: Select the position you wish to move to: (Enter -1 to go back)"))
      if move == -1:
         break
      for i in moves:
         if move == i:
            legal = True
   while move == -1:
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
      while legal == False:
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
      move = int(input("You are in check, please try again"))
      b[player] = board[player]
      b[move] = board[move]
   Move(board,player,move)
   printBoard(board)
   if checkmate(board,20):
      print("WHITE WINS THE GAME")
      break

   opponent = chessPlayer(board,20)
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
   Move(board,int(opponent[1][0]),int(opponent[1][1]))
   printBoard(board)
   if checkmate(board,10):
      print("BLACK WINS THE GAME")
      break
