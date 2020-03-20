from chessPlayer_queue import *

class tree:
   def __init__(self,x):
      self.store = [x,[]]
      self.counter = 0
      self.root = x
      self.level = 0;

   def AddSuccessor(self,x):
      self.store[1] = self.store[1] + [x]
      self.counter = self.counter + 1
      return True

   def getcount(self):
      return self.counter

   def getpos(self):
      return self.store[0][0]

   def getmove(self):
      return self.store[0][1]

   def getrating(self):
      return self.store[0][2]

   def GetSuccessors(self):
      return self.store[1]

   def Print_DepthFirst(self):
      self.Print_DepthFirst_spaces("")
      return True

   def Print_DepthFirst_spaces(self,spaces):
      print(spaces+str(self.store[0]))
      for i in self.store[1]:
         i.Print_DepthFirst_spaces(spaces+"   ")
      return True

   def Get_LevelOrder(self):
      x = queue()
      x.enqueue(self.store)
      accum = []
      while True:
         l = x.dequeue()
         if(l[0] == False):
            break
         a = l[1]
         accum = accum + [(a[0])]
         for i in a[1]:
            x.enqueue(i.store)
      return accum