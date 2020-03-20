class queue:
    def __init__(self):
        self.store=[]
        self.counter = 0

    def enqueue(self,value):
        self.store = self.store + [value]
        self.counter = self.counter + 1
        return self.counter

    def dequeue(self):
        if (self.counter == 0):
            return [False,0]
        else:
            r= self.store[0]
            self.counter = self.counter-1
            self.store = self.store[1:]
            return [True,r]