from chessPlayer_tree import *

def genBoard(): # function used to generate the board, different values correspond to different pieces
   board = [13,11,12,15,14,12,11,13,
           10,10,10,10,10,10,10,10,
           0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,
           20,20,20,20,20,20,20,20,
           23,21,22,25,24,22,21,23]
   return board

def printBoard(board):
   if len(board) != 64:
      return False
   b = []
   index = 0
   for i in board: # prints the respective piece based on the associated index
      if i == 10:
         b = b + ['wp']
      elif i == 11:
         b = b + ['wk']
      elif i == 12:
         b = b + ['wb']
      elif i == 13:
         b = b + ['wr']
      elif i == 14:
         b = b + ['wq']
      elif i == 15:
         b = b + ['wK']
      elif i == 20:
         b = b + ['bp']
      elif i == 21:
         b = b + ['bk']
      elif i == 22:
         b = b + ['bb']
      elif i == 23:
         b = b + ['br']
      elif i == 24:
         b = b + ['bq']
      elif i == 25:
         b = b + ['bK']
      else:
         if index%2 == 0 and (-1<index<8 or 15<index<24 or 31<index<40 or 47<index<56): # prints the black and white empty squares as required
            b = b + ['#']
         elif index%2 == 0 and (7<index<16 or 23<index<32 or 39<index<48 or 55<index):
            b = b + ['_']
         elif index%2 != 0 and (-1<index<8 or 15<index<24 or 31<index<40 or 47<index<56):
            b = b + ['_']
         elif index%2 != 0 and (7<index<16 or 23<index<32 or 39<index<48 or 55<index):
            b = b + ['#']
      index += 1
   r = ''
   for i in range(56,64,1): # prints the entire list that signifies the board
      if b[i] == '#' or b[i] == '_':
         r = b[i] + '  ' + r + '  '
      else:
         r = b[i] + ' ' + r + ' '
   print(r)
   r = ''
   for i in range(48, 56, 1):
      if b[i] == '#' or b[i] == '_':
         r = b[i] + '  ' + r + '  '
      else:
         r = b[i] + ' ' + r + ' '
   print(r)
   r = ''
   for i in range(40, 48, 1):
      if b[i] == '#' or b[i] == '_':
         r = b[i] + '  ' + r + '  '
      else:
         r = b[i] + ' ' + r + ' '
   print(r)
   r = ''
   for i in range(32, 40, 1):
      if b[i] == '#' or b[i] == '_':
         r = b[i] + '  ' + r + '  '
      else:
         r = b[i] + ' ' + r + ' '
   print(r)
   r = ''
   for i in range(24, 32, 1):
      if b[i] == '#' or b[i] == '_':
         r = b[i] + '  ' + r + '  '
      else:
         r = b[i] + ' ' + r + ' '
   print(r)
   r = ''
   for i in range(16, 24, 1):
      if b[i] == '#' or b[i] == '_':
         r = b[i] + '  ' + r + '  '
      else:
         r = b[i] + ' ' + r + ' '
   print(r)
   r = ''
   for i in range(8, 16, 1):
      if b[i] == '#' or b[i] == '_':
         r = b[i] + '  ' + r + '  '
      else:
         r = b[i] + ' ' + r + ' '
   print(r)
   r = ''
   for i in range(0, 8, 1):
      if b[i] == '#' or b[i] == '_':
         r = b[i] + '  ' + r + '  '
      else:
         r = b[i] + ' ' + r + ' '
   print(r)


def GetPlayerPositions(board, player): # returns the various positions that the player's pieces are located at
   positions = []
   index = 0
   for i in board:
      if player + 10 > i >= player:
         positions = positions + [index]
      index += 1
   return positions

def GetPieceLegalMoves(board, position): # returns the possible moves available for the piece selected
   moves = []
   if board[position] == 0:
      return False
   if board[position] == 10:
      return PawnLegalMoves(board, position, 10)
   if board[position] == 20:
      return PawnLegalMoves(board, position, 20)
   if board[position] == 11:
      return KnightLegalMoves(board, position, 10)
   if board[position] == 21:
      return KnightLegalMoves(board, position, 20)
   if board[position] == 12:
      return BishopLegalMoves(board, position, 10)
   if board[position] == 22:
      return BishopLegalMoves(board, position, 20)
   if board[position] == 13:
      return RookLegalMoves(board, position, 10)
   if board[position] == 23:
      return RookLegalMoves(board, position, 20)
   if board[position] == 14:
      return QueenLegalMoves(board, position, 10)
   if board[position] == 24:
      return QueenLegalMoves(board, position, 20)
   if board[position] == 15:
      return KingLegalMoves(board, position, 10)
   if board[position] == 25:
      return KingLegalMoves(board, position, 20)

def IsPositionUnderThreat(board, position, player): # function used to determine a piece at a certain position is under threat from the opposing player
   if player == 10:
      other = GetPlayerPositions(board,20)
      if len(other) > 0:
         for i in other:
            if board[i] == 25:
               moves = KingAndKing(board,i,20)
            else:
               moves = GetPieceLegalMoves(board,i)
            if len(moves) > 0:
               for j in moves:
                  if j == position:
                     return True
   if player == 20:
      other = GetPlayerPositions(board,10)
      if len(other) > 0:
         for i in other:
            if board[i] == 15:
               moves = KingAndKing(board,i,10)
            else:
               moves = GetPieceLegalMoves(board,i)
            if len(moves) > 0:
               for j in moves:
                  if j == position:
                     return True
   return False


def check(board, color): # determines if the king is currently under check
   king = 0
   for i in range(0,len(board),1):
      if board[i] == color + 5:
         king = i
   return IsPositionUnderThreat(board, king, color)

def checkmate(board, color): # determines if the king is under checkmate (king is unable to move out of the check position and no other piece is able to protect the king from check)
   b = list(board)
   if color == 10:
      positions = GetPlayerPositions(board, 10)
      for i in positions:
         if b[i] != 15:
            moves = GetPieceLegalMoves(board,i)
            for j in moves:
               b[j] = b[i]
               b[i] = 0
               if not check(b, color):
                  return False
               b[i] = board[i]
               b[j] = board[j]
   if color == 20:
      positions = GetPlayerPositions(board, 20)
      for i in positions:
         if b[i] != 25:
            moves = GetPieceLegalMoves(board,i)
            for j in moves:
               b[j] = b[i]
               b[i] = 0
               if not check(b, color):
                  return False
               b[i] = board[i]
               b[j] = board[j]
   king = 0
   for i in range(0,len(board),1):
      if board[i] == color + 5:
         king = i
   kingposition = GetPieceLegalMoves(board,king)
   if len(GetPieceLegalMoves(board, king)) == 0:
      return True
   return False

def other(color):
   if color == 10:
      return 25
   if color == 20:
      return 15

def KingAndKing(board, position, color): # function that determines the movement of a king relative to the possible moves of the opposing king
   otherking = 0
   otherkingmoves = []
   moves = []
   for i in board:
      if i == other(color):
         otherking = i
   if otherking + 8 < 64:
      otherkingmoves = otherkingmoves + [otherking + 8]
   if otherking + 9 < 64 and (otherking + 1) % 8 != 0:
      otherkingmoves = otherkingmoves + [otherking + 9]
   if otherking - 7 < 64 and (otherking + 1) % 8 != 0:
      otherkingmoves = otherkingmoves + [otherking - 7]
   if otherking - 9 < 64 and (otherking) % 8 != 0:
      otherkingmoves = otherkingmoves + [otherking - 9]
   if otherking + 7 < 64 and (otherking) % 8 != 0:
      otherkingmoves = otherkingmoves + [otherking + 7]
   if otherking - 8 > 0:
      otherkingmoves = otherkingmoves + [otherking - 8]
   if (otherking + 1) % 8 != 0:
      otherkingmoves = otherkingmoves + [otherking + 1]
   if otherking % 8 != 0:
      otherkingmoves = otherkingmoves + [otherking - 1]

   if position + 8 < 64:
      moves = moves + [position + 8]
   if position + 9 < 64 and (position + 1) % 8 != 0:
      moves = moves + [position + 9]
   if position - 7 < 64 and (position + 1) % 8 != 0:
      moves = moves + [position - 7]
   if position - 9 < 64 and (position) % 8 != 0:
      moves = moves + [position - 9]
   if position + 7 < 64 and (position) % 8 != 0:
      moves = moves + [position + 7]
   if position - 8 > 0:
      moves = moves + [position - 8]
   if (position + 1) % 8 != 0:
      moves = moves + [position + 1]
   if position % 8 != 0:
      moves = moves + [position - 1]

   count = 0
   moves1 = []
   for i in moves:
      for j in otherkingmoves:
         if i != j:
            count = count + 1
      if count == len(otherkingmoves):
         moves1 = moves1 + [i]
   return moves1


def KingLegalMoves(board, position, color): # returns the legal moves available to the king at a certain position (not allowing the king to travel to a position of threat)
   moves = []
   b = list(board)
   if position + 8 < 64 and not (color <= board[position + 8] <= color + 5):
      b[position + 8] = color + 5
      b[position] = 0
      if not IsPositionUnderThreat(b, position + 8, color):
         moves = moves + [position + 8]
      b[position] = board[position]
      b[position + 8] = board[position + 8]
   if position + 9 < 64 and not (color <= board[position + 9] <= color + 5) and (position + 1) % 8 != 0:
      b[position + 9] = color + 5
      b[position] = 0
      if not IsPositionUnderThreat(b, position + 9, color):
         moves = moves + [position + 9]
      b[position] = board[position]
      b[position + 9] = board[position + 9]
   if position + 7 < 64 and not (color <= board[position + 7] <= color + 5) and (position) % 8 != 0:
      b[position + 7] = color + 5
      b[position] = 0
      if not IsPositionUnderThreat(b, position + 7, color):
         moves = moves + [position + 7]
      b[position] = board[position]
      b[position + 7] = board[position + 7]
   if (position + 1) % 8 != 0 and not (color <= board[position + 1] <= color + 5):
      b[position + 1] = color + 5
      b[position] = 0
      if not IsPositionUnderThreat(b, position + 1, color):
         moves = moves + [position + 1]
      b[position] = board[position]
      b[position + 1] = board[position + 1]
   if position - 7 > 0 and not (color <= board[position - 7] <= color + 5) and (position + 1) % 8 != 0:
      b[position - 7] = color + 5
      b[position] = 0
      if not IsPositionUnderThreat(b, position - 7, color):
         moves = moves + [position - 7]
      b[position] = board[position]
      b[position - 7] = board[position - 7]
   if position - 9 > 0 and not (color <= board[position - 9] <= color + 5) and (position) % 8 != 0:
      b[position - 9] = color + 5
      b[position] = 0
      if not IsPositionUnderThreat(b, position - 9, color):
         moves = moves + [position - 9]
      b[position] = board[position]
      b[position - 9] = board[position - 9]
   if position % 8 != 0 and not (color <= board[position - 1] <= color + 5):
      b[position - 1] = color + 5
      b[position] = 0
      if not IsPositionUnderThreat(b, position - 1, color):
         moves = moves + [position - 1]
      b[position] = board[position]
      b[position - 1] = board[position - 1]
   if position - 8 > 0 and not (color <= board[position - 8] <= color + 5):
      b[position - 8] = color + 5
      b[position] = 0
      if not IsPositionUnderThreat(b, position - 8, color):
         moves = moves + [position - 8]
      b[position] = board[position]
      b[position - 8] = board[position - 8]
   return moves


def QueenLegalMoves(board, position, color): # returns the moves available to the queen at a certain position
   moves = []
   rook = RookLegalMoves(board, position, color)
   bishop = BishopLegalMoves(board, position, color)
   moves = rook + bishop
   return moves

def RookLegalMoves(board, position, color): # returns the moves available to the rook at a certain position
   moves = []
   pos = position
   if pos + 8 < 64:
      while pos+8<64 and pos+8>0 and board[pos+8] == 0:
         pos = pos + 8
         moves = moves + [pos]
         if pos + 8 > 64:
            break
      if pos + 8 < 64 and board[pos+8] > 19 and color == 10:
         moves = moves + [pos + 8]
      elif pos + 8 < 64 and board[pos+8] < 20 and color == 20:
         moves = moves + [pos + 8]
   pos = position
   if pos - 8 > 0:
      while pos-8>0 and board[pos-8] == 0:
         pos = pos - 8
         moves = moves + [pos]
         if pos - 8 < 0:
            break
      if pos - 8 > 0 and board[pos-8] > 19 and color == 10:
         moves = moves + [pos - 8]
      elif pos - 8 > 0 and board[pos-8] < 20 and color == 20:
         moves = moves + [pos - 8]
   pos = position
   if pos + 1 < 64:
      while pos + 1 < 64 and (pos+1)%8 != 0 and board[pos+1] == 0:
         pos = pos + 1
         moves = moves + [pos]
         if pos + 1 > 64:
            break
      if pos + 1 < 64 and board[pos+1] > 19 and (pos+1)%8 != 0 and color == 10:
         moves = moves + [pos + 1]
      elif pos + 1 < 64 and board[pos+1] < 20 and (pos+1)%8 != 0 and color == 20:
         moves = moves + [pos + 1]
   pos = position
   if pos - 1 > 0:
      while pos - 1 > 0 and (pos)%8 != 0 and board[pos-1] == 0:
         pos = pos - 1
         moves = moves + [pos]
         if pos - 1 < 0:
            break
      if pos - 1 > 0 and board[pos-1] > 19 and (pos)%8 != 0 and color == 10:
         moves = moves + [pos - 1]
      elif pos - 1 > 0 and board[pos-1] < 20 and (pos)%8 != 0 and color == 20:
         moves = moves + [pos - 1]
   return moves

def BishopLegalMoves(board, position, color): # returns the moves available to the bishop at a certain position
   moves = []
   pos = position
   if pos + 9 < 64:
      while pos + 9 < 64 and (board[pos + 9] == 0) and ((pos + 1) % 8 != 0):
         pos = pos + 9
         moves = moves + [pos]
         if pos + 9 > 64:
            break
      if pos + 9 < 64 and board[pos + 9] > 19 and (pos + 1) % 8 != 0 and color == 10:
         moves = moves + [pos + 9]
      elif pos + 9 < 64 and board[pos + 9] < 20 and (pos + 1) % 8 != 0 and color == 20:
         moves = moves + [pos + 9]
   pos = position
   if pos - 7 > 0:
      while pos - 7 > 0 and (board[pos - 7] == 0) and ((pos + 1) % 8 != 0):
         pos = pos - 7
         moves = moves + [pos]
         if pos - 7 < 0:
            break
      if pos - 7 > 0 and board[pos - 7] > 19 and (pos + 1) % 8 != 0 and color == 10:
         moves = moves + [pos - 7]
      elif pos - 7 > 0 and board[pos - 7] < 20 and (pos + 1) % 8 != 0 and color == 20:
         moves = moves + [pos - 7]
   pos = position
   if pos + 7 < 64:
      while pos + 7 < 64 and (board[pos + 7] == 0) and (pos % 8 != 0):
         pos = pos + 7
         moves = moves + [pos]
         if pos + 7 > 64:
            break
      if pos + 7 < 64 and board[pos + 7] > 19 and (pos) % 8 != 0 and color == 10:
         moves = moves + [pos + 7]
      elif pos + 7 < 64 and board[pos + 7] < 20 and (pos) % 8 != 0 and color == 20:
         moves = moves + [pos + 7]
   pos = position
   if pos - 9 > 0:
      while pos - 9 > 0 and (board[pos - 9] == 0) and (pos % 8 != 0):
         pos = pos - 9
         moves = moves + [pos]
         if pos - 9 < 0:
            break
      if pos - 9 > 0 and board[pos - 9] > 19 and (pos) % 8 != 0 and color == 10:
         moves = moves + [pos - 9]
      elif pos - 9 > 0 and board[pos - 9] < 20 and (pos) % 8 != 0 and color == 20:
         moves = moves + [pos - 9]
   return moves


def KnightLegalMoves(board, position, color): # returns the moves available to the knight at a certain position
   moves = []
   if color == 10:
      if position + 17 < 64:
         if (position + 1) % 8 != 0 and ((board[position + 17] == 0) or (board[position + 17] > 19)):
            moves = moves + [position + 17]
         if (position) % 8 != 0 and ((board[position + 15] == 0) or (board[position + 15] > 19)):
            moves = moves + [position + 15]
      if position - 17 > 0:
         if (position + 1) % 8 != 0 and ((board[position - 17] == 0) or (board[position - 17] > 19)):
            moves = moves + [position - 17]
            if (position) % 8 != 0 and ((board[position - 15] == 0) or (board[position - 15] > 19)):
               moves = moves + [position - 15]
         if position + 10 < 64 and ((board[position + 10] == 0) or (board[position + 10] > 19)):
            if (position + 2) % 8 != 0 and ((board[position + 10] == 0) or (board[position + 10] > 19)):
               moves = moves + [position + 10]
            if (position - 1) % 8 != 0 and ((board[position + 6] == 0) or (board[position + 6] > 19)):
               moves = moves + [position + 6]
         if position - 10 > 0:
            if (position + 2) % 8 != 0 and ((board[position - 10] == 0) or (board[position - 10] > 19)):
               moves = moves + [position - 10]
            if (position - 1) % 8 != 0 and ((board[position - 6] == 0) or (board[position - 6] > 19)):
               moves = moves + [position - 6]
         if color == 20:
            if position + 17 < 64:
               if (position + 1) % 8 != 0 and (board[position + 17] < 20):
                  moves = moves + [position + 17]
               if (position) % 8 != 0 and (board[position + 15] < 20):
                  moves = moves + [position + 15]
            if position - 17 > 0:
               if (position + 1) % 8 != 0 and (board[position - 17] < 0):
                  moves = moves + [position - 17]
               if (position) % 8 != 0 and (board[position - 15] < 0):
                  moves = moves + [position + 15]
            if position + 10 < 64:
               if (position + 2) % 8 != 0 and (board[position + 10] < 0):
                  moves = moves + [position + 10]
               if (position - 1) % 8 != 0 and (board[position + 6] < 0):
                  moves = moves + [position + 6]
            if position - 10 > 0:
               if (position + 2) % 8 != 0 and (board[position - 10] < 0):
                  moves = moves + [position - 10]
               if (position - 1) % 8 != 0 and (board[position - 6] == 0):
                  moves = moves + [position - 6]
         return moves

def PawnLegalMoves(board, position, color): # returns the moves available to a pawn at a certain position
   moves = []
   if color == 10:
      if board[position + 8] == 0:
         moves = moves + [position+8]
      if (position + 1)%8 == 0:
         if board[position + 7] >= 20:
            moves = moves + [position+7]
      if position%8 == 0:
         if board[position + 9] >= 20:
            moves = moves + [position+7]
      if (position%8 != 0) and ((position+1)%8 != 0):
         if board[position + 9] >= 20:
            moves = moves + [position+9]
         if board[position + 7] >= 20:
            moves = moves + [position+7]
      if position > 56:
         moves = []
   if color == 20:
      if board[position - 8] == 0:
         moves = moves + [position-8]
      if (position + 1)%8 == 0:
         if 16 > board[position - 9] > 0:
            moves = moves + [position-9]
      if position%8 == 0:
         if 16 > board[position - 7] > 0:
            moves = moves + [position-7]
      if (position%8 != 0) and ((position+1)%8 != 0):
         if 16 > board[position -9] > 0:
            moves = moves + [position-9]
         if 16 > board[position - 7] > 0:
            moves = moves + [position - 7]
      if position < 8:
         moves = []
   return moves

def Move(board, position1, position2): # moves a piece from position 1 to position 2
   board[position2] = board[position1]
   board[position1] = 0

def QueenMobility(board,position1,position2,color): # returns a value corresponding to the queen's ability to move around the board
   queen = 0
   initial = 0
   final = 0
   isqueen = False
   for i in range(0, len(board), 1):
      if board[i] == color + 4:
         queen = i
         isqueen = True
   if isqueen:
      initial = len(GetPieceLegalMoves(board,queen))/10
   b = list(board)
   b[position2] = b[position1]
   b[position1] = 0
   queen = 0
   isqueen = False
   for i in range(0, len(b), 1):
      if b[i] == color + 4:
         queen = i
         isqueen = True
   if isqueen:
      final = len(GetPieceLegalMoves(b,queen))/10
   return final-initial

def RookMobility(board,position1,position2,color): # returns a value corresponding to the rook's ability to move around the board
   rook1 = 0
   rook2 = 0
   isrook1 = False
   isrook2 = False
   initial = 0
   final = 0
   for i in range(0, len(board), 1):
      if (board[i] == color + 3) and not isrook1 and not isrook2:
         rook1 = i
         isrook1 = True
      elif (board[i] == color + 3) and isrook1 and not isrook2:
         rook2 = i
         isrook2 = True
   if isrook1 and not isrook2:
      initial = len(GetPieceLegalMoves(board,rook1))/10
   elif isrook1 and isrook2:
      initial = len(GetPieceLegalMoves(board,rook1) + GetPieceLegalMoves(board,rook2))/10
   rook1 = 0
   rook2 = 0
   isrook1 = False
   isrook2 = False
   b = list(board)
   b[position2] = b[position1]
   b[position1] = 0
   for i in range(0, len(b), 1):
      if (b[i] == color + 3) and not isrook1 and not isrook2:
         rook1 = i
         isrook1 = True
      elif (b[i] == color + 3) and isrook1 and not isrook2:
         rook2 = i
         isrook2 = True
   if isrook1 and not isrook2:
      final = len(GetPieceLegalMoves(b,rook1))/10
   elif isrook1 and isrook2:
      final = len(GetPieceLegalMoves(b,rook1) + GetPieceLegalMoves(b,rook2))/10
   return final-initial

def BishopMobility(board,position1,position2,color): # returns a value corresponding to the bishop's ability to move around the board
   initial = 0
   final = 0
   bishop1 = 0
   bishop2 = 0
   isbishop1 = False
   isbishop2 = False
   for i in range(0, len(board), 1):
      if (board[i] == color + 2) and (not isbishop1) and (not isbishop2):
         bishop1 = i
         isbishop1 = True
      elif (board[i] == color + 2) and isbishop1 and not isbishop2:
         bishop2 = i
         isbishop2 = True
   if isbishop1 and not isbishop2:
      initial = len(GetPieceLegalMoves(board,bishop1))
   elif isbishop1 and isbishop2:
      initial = len(GetPieceLegalMoves(board,bishop1) + GetPieceLegalMoves(board,bishop2))/10
   bishop1 = 0
   bishop2 = 0
   isbishop1 = False
   isbishop2 = False
   b = list(board)
   b[position2] = b[position1]
   b[position1] = 0
   for i in range(0, len(board), 1):
      if (b[i] == color + 2) and (not isbishop1) and (not isbishop2):
         bishop1 = i
         isbishop1 = True
      elif (b[i] == color + 2) and isbishop1 and not isbishop2:
         bishop2 = i
         isbishop2 = True
   if isbishop1 and not isbishop2:
      final = len(GetPieceLegalMoves(b,bishop1))
   elif isbishop1 and isbishop2:
      final = len(GetPieceLegalMoves(b,bishop1) + GetPieceLegalMoves(b,bishop2))/10
   return final-initial

def KingProtection(board,position1,position2,color): # returns a value associated with hoe well the king is protected by its surrounding pirces
   initial = 0
   final = 0
   i = 0;
   protect = 0;
   available = 0;
   for j in range(0, len(board), 1):
      if board[j] == color + 5:
         i = j
   if i + 9 < 64 and (i+1)%8 != 0:
      available = available + 1
      if board[i+9] > 0:
         protect = protect + 1
   if i - 7 > 0 and (i+1)%8 != 0:
      available = available + 1
      if board[i-7] > 0:
         protect = protect + 1
   if i + 1 < 64 and (i+1)%8 != 0:
      available = available + 1
      if board[i+1] > 0:
         protect = protect + 1
   if i - 9 > 0 and (i)%8 != 0:
      available = available + 1
      if board[i-9] > 0:
         protect = protect + 1
   if i + 7 < 64 and (i)%8 != 0:
      available = available + 1
      if board[i+7] > 0:
         protect = protect + 1
   if i - 1 > 0 and (i)%8 != 0:
      available = available + 1
      if board[i-1] > 0:
         protect = protect + 1
   if i + 8 < 64:
      available = available + 1
      if board[i+8] > 0:
         protect = protect + 1
   if i - 8 > 0:
      available = available + 1
      if board[i-8] > 0:
         protect = protect + 1
   initial = protect/available

   i = 0;
   protect = 0;
   available = 0;
   b = list(board)
   b[position2] = b[position1]
   b[position1] = 0
   for j in range(0, len(b), 1):
      if b[j] == color + 5:
         i = j
   if i + 9 < 64 and (i+1)%8 != 0:
      available = available + 1
      if b[i+9] > 0:
         protect = protect + 1
   if i - 7 > 0 and (i+1)%8 != 0:
      available = available + 1
      if b[i-7] > 0:
         protect = protect + 1
   if i + 1 < 64 and (i+1)%8 != 0:
      available = available + 1
      if b[i+1] > 0:
         protect = protect + 1
   if i - 9 > 0 and (i)%8 != 0:
      available = available + 1
      if b[i-9] > 0:
         protect = protect + 1
   if i + 7 < 64 and (i)%8 != 0:
      available = available + 1
      if b[i+7] > 0:
         protect = protect + 1
   if i - 1 > 0 and (i)%8 != 0:
      available = available + 1
      if b[i-1] > 0:
         protect = protect + 1
   if i + 8 < 64:
      available = available + 1
      if b[i+8] > 0:
         protect = protect + 1
   if i - 8 > 0:
      available = available + 1
      if b[i-8] > 0:
         protect = protect + 1
   final = protect/available
   return final-initial

def CheckValue(board, position1, position2, color): # value associated with putting the other team in check
   if check(board,color) == False:
      return 0
   moves = GetPieceLegalMoves(board,position1)
   b = list(board)
   b[position2] = b[position1]
   b[position1] = 0
   if check(b,color) == False:
      return 1000
   return -1000

def CheckMateValue(board, position1, position2, color): # value associated with putting the other team under check mate
   b = list(board)
   b[position2] = b[position1]
   b[position1] = 0
   if checkmate(b,other(color)) == True:
      return 80
   return 0

def KillValue(board, position1, position2, color): # value associated with taking an opposing piece (also factors in sacrificing the piece selected if the opposing piece is of greater value)
   if board[position2] == 0:
      return 0
   value = 0
   maximum = 0
   b = list(board)
   b[position2] = b[position1]
   b[position1] = 0
   if not IsPositionUnderThreat(b,position2,color):
      value = board[position2]%10
      return value
   elif IsPositionUnderThreat(b,position2,color):
      if board[position2]%10 == 4:
         return 10*((board[position2]%10) - (board[position1]%10))
      return 5*(board[position2]%10) - (board[position1]%10)

def InThreat(board, position1, position2, color): # determines if the given position is under threat by the opposing team
   b = list(board)
   b[position2] = b[position1]
   b[position1] = 0
   if IsPositionUnderThreat(b,position2,color) == True:
      if b[position2]%10 == 4:
         l = -10 * (b[position2]%10)
         return(l)
      return(-10 * b[position2]%10)
   else:
      return 0

def Protect(board, position1, position2, color): # value associated with protecting a particular piece of value
   if IsPositionUnderThreat(board,position1,color) == False:
      return 0
   b = list(board)
   b[position2] = b[position1]
   b[position1] = 0
   if IsPositionUnderThreat(b,position2,color):
      if b[position2]%10 == 4:
         return -80
      else:
         return(b[position2]%10)
   if IsPositionUnderThreat(b,position2,color) == False:
      if b[position2]%10 == 4:
         return 80
      else:
         return(b[position2]%10)

def other(color):
   if color == 10:
      return 20
   elif color == 20:
      return 10

def top5(board,color,x): # function that returns the top 5 possible moves the computer can make associated with ranking
   #x = tree([color,0])
   top5 = []
   players = GetPlayerPositions(board,color)
   for j in players:
      moves = GetPieceLegalMoves(board,j)
      for i in moves:
         if check(board,color) == True:
            b = list(board)
            b[i] = b[j]
            b[j] = 0
            if check(b,color) == False:
               top5 = top5 + [rating(board,j,i,color)[2]]
         else:
            top5 = top5 + [rating(board,j,i,color)[2]]
   top5.sort()
   if len(top5) > 3:
      top5 = top5[len(top5)-3:]
   for j in players:
      moves = GetPieceLegalMoves(board,j)
      for i in moves:
         l = True
         for a in top5:
            if rating(board,j,i,color)[2] == a and x.getcount() < 3 and l:
               l = False
               r = tree(rating(board,j,i,color))
               x.AddSuccessor(r)
   return x

def genBestMoveTree(board,color,x): # tree structure that is used to evaluate the best possible moves at each level
   accum = x.GetSuccessors()
   for i in accum:
      b = list(board)
      b[i.getmove()] = b[i.getpos()]
      b[i.getpos()] = 0
      top5(b,other(color),i)
      accum1 = i.GetSuccessors()
      for j in accum1:
         b1 = list(b)
         b1[j.getmove()] = b1[j.getpos()]
         b1[j.getpos()] = 0
         top5(b1,color,j)
         accum2 = j.GetSuccessors()
         for k in accum2:
            b2 = list(b1)
            b2[k.getmove()] = b2[k.getpos()]
            b2[k.getpos()] = 0
            top5(b2,other(color),k)
            accum3 = k.GetSuccessors()
            for l in accum3:
               b3 = list(b2)
               b3[l.getmove()] = b3[l.getpos()]
               b3[l.getpos()] = 0
               top5(b3,color,l)
   return x

def chessPlayer(board,player): # function that utilizes the tree structure and checks multiple levels in order to determine the best possible move while factoring in future potential
   color = player
   x = tree([color,0])
   top5(board,color,x)
   accum = x.GetSuccessors()
   for i in accum:
      b = list(board)
      b[i.getmove()] = b[i.getpos()]
      b[i.getpos()] = 0
      top5(b,other(color),i)
      accum1 = i.GetSuccessors()
      for j in accum1:
         b1 = list(b)
         b1[j.getmove()] = b1[j.getpos()]
         b1[j.getpos()] = 0
         top5(b1,color,j)
         accum2 = j.GetSuccessors()
         for k in accum2:
            b2 = list(b1)
            b2[k.getmove()] = b2[k.getpos()]
            b2[k.getpos()] = 0
            top5(b2,other(color),k)
            accum3 = k.GetSuccessors()
            for l in accum3:
               b3 = list(b2)
               b3[l.getmove()] = b3[l.getpos()]
               b3[l.getpos()] = 0
               top5(b3,color,l)
   moves1 = x.Get_LevelOrder()

   move1 = 0
   move2 = 0
   move3 = 0
   count1 = 0
   count2 = 0
   count3 = 0
   print(len(x.GetSuccessors()))
   if len(x.GetSuccessors()) == 1:
      return [True, moves1[1][0:2], moves1[1], moves1]
   tree1 = x.GetSuccessors()[0]
   if len(x.GetSuccessors()) > 1:
      tree2 = x.GetSuccessors()[1]
      if len(x.GetSuccessors()) == 3:
         tree3 = x.GetSuccessors()[2]
   for i in tree1.GetSuccessors():
      move1 = move1 - i.getrating()
      count1 = count1 + 1
      for j in i.GetSuccessors():
         move1 = move1 + j.getrating()
         count1 = count1 + 1
         for k in j.GetSuccessors():
            move1 = move1 - k.getrating()
            count1 = count1 + 1
            for l in k.GetSuccessors():
               move1 = move1 + l.getrating()
               count1 = count1 + 1
   if len(x.GetSuccessors()) > 1:
      for i in tree2.GetSuccessors():
         move2 = move2 - i.getrating()
         count2 = count2 + 1
         for j in i.GetSuccessors():
            move2 = move2 + j.getrating()
            count2 = count2 + 1
            for k in j.GetSuccessors():
               move2 = move2 - k.getrating()
               count2 = count2 + 1
               for l in k.GetSuccessors():
                  move2 = move2 + l.getrating()
                  count2 = count2 + 1
   if len(x.GetSuccessors()) == 3:
      for i in tree3.GetSuccessors():
         move3 = move3 - i.getrating()
         count3 = count3 + 1
         for j in i.GetSuccessors():
            move3 = move3 + j.getrating()
            count3 = count3 + 1
            for k in j.GetSuccessors():
               move3 = move3 - k.getrating()
               count3 = count3 + 1
               for l in k.GetSuccessors():
                  move3 = move3 + l.getrating()
                  count3 = count3 + 1

   move1 = move1 + 5*x.GetSuccessors()[0].getrating()
   count1 = count1 + 1
   if len(x.GetSuccessors()) > 1:
      move2 = move2 + 5*x.GetSuccessors()[1].getrating()
      count2 = count2 + 2
   if len(x.GetSuccessors()) == 3:
      move3 = move3 + 5*x.GetSuccessors()[2].getrating()
      count3 = count3 + 1
   if count1 != 0:
      move1 = move1 / count1
   if count2 != 0:
      move2 = move2 / count2
   if count3 != 0:
      move3 = move3 / count3
   if len(x.GetSuccessors()) == 3:
      if move1 >= (move2 and move3):
         return[True,moves1[1][0:2],moves1[1],moves1]
      elif move2 >= (move1 and move3):
         return[True,moves1[2][0:2],moves1[2],moves1]
      elif move3 >= (move2 and move1):
         return[True,moves1[3][0:2],moves1[3],moves1]
   elif len(x.GetSuccessors()) == 2:
      if move1 >= move2:
         return[True,moves1[1][0:2],moves1[1],moves1]
      else:
         return[True,moves1[2][0:2],moves1[2],moves1]

def rating(board,position1,position2,color): # overall rating system of a move relative to the current state of the board
   queenmobility = QueenMobility(board,position1,position2,color)
   rookmobility = RookMobility(board,position1,position2,color)
   bishopmobility = BishopMobility(board,position1,position2,color)
   kingprotection = KingProtection(board,position1,position2,color)
   killvalue = KillValue(board,position1,position2,color)
   checkvalue = CheckValue(board,position1,position2,color)
   checkmatevalue = CheckMateValue(board,position1,position2,color)
   protect = Protect(board,position1,position2,color)
   inthreat = InThreat(board,position1,position2,color)
   rating = float(protect + queenmobility + rookmobility + bishopmobility + kingprotection + killvalue+checkmatevalue+inthreat)
   return [position1,position2,rating]

