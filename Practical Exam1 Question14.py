# Write and know the simple queue, circular queue, and stack classes that we wrote about in class.

# Stack
class Stack:
    def __init__(self):
        self.list = []
    def push(self, val): self.list.append(val)
    def pop(self):
        if not self.list: print("Stack is empty!"); return
        return self.list.pop()
    def show(self): print(f"Stack: {self.list}")


# Simple Queue 
class SimpleQueue:
    def __init__(self):
        self.list = []
    def enqueue(self, val): self.list.append(val)
    def dequeue(self):
        if not self.list: print("Queue is empty!"); return
        return self.list.pop(0)
    def show(self): print(f"Simple Queue: {self.list}")


# Circular Queue
class CircularQueue:
    def __init__(self, size=5):
        self.list = [None]*size
        self.front = -1
        self.rear = -1
        self.size = size

    def enqueue(self, val):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full!"); return
        if self.front == -1: self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.list[self.rear] = val

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty!"); return
        val = self.list[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return val

    def show(self):
        print(f"Circular Queue: {self.list}")



# Test:

print("Stack")
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.show()
print("Pop:", s.pop())
s.show()

print("\nSimple Queue")
sq = SimpleQueue()
sq.enqueue("A")
sq.enqueue("B")
sq.show()
print("Dequeue:", sq.dequeue())
sq.show()

print("\nCircular Queue")
cq = CircularQueue(4)
cq.enqueue("X")
cq.enqueue("Y")
cq.enqueue("Z")
cq.show()
print("Dequeue:", cq.dequeue())
cq.enqueue("W")
cq.show()
