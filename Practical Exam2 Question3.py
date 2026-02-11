# Implement a Circular Queue class with a Doubly Linked List.

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Circular_Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue Method
    def enqueue(self,x):
        a = Node(x)
        if self.front is None:      # Exception Case: Queue empty
            self.front = self.rear = a
            a.next = a
            a.prev = a
        else:
            a.prev = self.rear
            a.next = self.front
            self.rear.next = a
            self.front.prev = a
            self.rear = a

    # Dequeue Method
    def dequeue(self):
        if self.front is None:      # Exception Case: Queue empty
            print("Queue is empty!")
            return
        if self.front == self.rear:      # Exception Case: Queue has only one member
            del self.front
            self.front = self.rear = None
            return
        a = self.front
        self.front = a.next
        self.front.prev = self.rear
        self.rear.next = self.front
        del a

    # Show Method
    def show(self):
        if self.front is None:
            print("Queue is empty!")
            return
        c = self.front
        while True:
            print(c.data)
            c = c.next
            if c == self.front:
                break