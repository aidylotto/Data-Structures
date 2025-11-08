# Queue

class queue:
    def __init__(self,max = 10):
        self.list = [] * max
        self.front = -1
        self.rear = -1

    # Insert Method        
    def insert(self,x):
        if self.rear >= len(self.list)-1:     # Exception Case (Queue being full)
            print("Queue is full!")
            return
        if self.front == -1:     # Exception Case (Queue being empty)
            self.front = 0
            self.rear = 0
            self.list[self.rear] = x
            return
        self.rear += 1
        self.list[self.rear] = x
        
    # Delete Method    
    def delete(self):
        if self.front == -1:     # Exception Case (Queue being empty)
            print("Queue is empty.")
            return
        if self.front == self.rear:     # Exception Case (Having only one member in the queue)
            k = self.list[self.rear]
            self.rear = -1
            self.front = -1
            return k
        k = self.list[self.front]
        self.front += 1
        return k
    
# Circular Queue
class Circular_Queue:
    def __init__(self,max):
        self.list = [] * max
        self.rear = -1
        self.front = -1

    # Insert Method    
    def insert(self,x):
        if (self.rear + 1) % len(self.list) == self.front:     # Exception Case (Queue being full)
            print("Queue is full")
            return
        if self.front == -1:     # Exception Case (Queue being empty)
            self.front = 0
            self.list[0] = x
            self.rear = 0
            return
        self.rear = (self.rear + 1) % len(self.list)
        self.list[self.rear] = x
    
    # Delete Method        
    def delete(self):
        if self.front == -1:     # Exception Case (Queue being empty)
            print("Queue is empty.")
            return
        if self.front == self.rear:     # Exception Case (Having only one member in the queue)
            k = self.list[self.rear]
            self.rear = -1
            self.front = -1
            return k
        k = self.list[self.front]
        self.front = (self.front + 1) % len(self.list)
        return k