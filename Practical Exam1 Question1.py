# Add a method to the queue which would solve it's problem by calling it.

class Queue:
    def __init__(self, size):
        self.size = size
        self.list = [None]*size
        self.front = 0
        self.rear = -1

    def isEmpty(self):
        return self.rear < self.front

    def isFull(self):
        return self.rear == self.size - 1

    def enqueue(self, item):
        if not self.isFull():
            self.rear += 1
            self.list[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            data = self.list[self.front]
            self.front += 1
            return data

    def fix_queue(self):
        if self.front > 0:
            for i in range(self.front, self.rear + 1):
                self.list[i - self.front] = self.list[i]
            self.rear -= self.front
            self.front = 0


# Test:

q = Queue(5)
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
q.dequeue()   
q.fix_queue() 
print(q.list)
