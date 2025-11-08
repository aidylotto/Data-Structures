# Define a new class that inherits from the two classes, circular queue and stack, written in the class. It should also have a super method and not be similar to each other.

class Stack:
    def __init__(self):
        self.list = []

    def push(self, val):
        self.list.append(val)

    def pop(self):
        if not self.isEmpty():
            return self.list.pop()
        print("Stack is empty!")

    def peek(self):
        if not self.isEmpty():
            return self.list[-1]

    def isEmpty(self):
        return len(self.list) == 0

    def show(self):
        print(f"Stack: {self.list}")


class CircularQueue:
    def __init__(self, size=5):
        self.list = [None]*size
        self.front = -1
        self.rear = -1
        self.size = size

    def enqueue(self, val):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full!")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.list[self.rear] = val

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty!")
            return
        val = self.list[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return val

    def show(self):
        print(f"Queue: {self.list}")


class Hybrid(Stack, CircularQueue):
    def __init__(self, size=5):
        super().__init__()
        CircularQueue.__init__(self, size)
        self.name = "Hybrid Structure"

    def push_to_stack(self, val):
        self.push(val)

    def enqueue_to_queue(self, val):
        self.enqueue(val)

    def mixed_pop(self):
        if not self.isEmpty():
            return self.pop()
        else:
            return self.dequeue()

    def show_all(self):
        print(f"Stack: {self.list}")
        print(f"Queue: {self.list}")
        print(f"Structure type: {self.name}")



# Test:

h = Hybrid(4)
h.push_to_stack(10)
h.push_to_stack(20)
h.enqueue_to_queue('A')
h.enqueue_to_queue('B')
h.show_all()
print(f"Mixed pop: {h.mixed_pop()}")
h.show_all()
