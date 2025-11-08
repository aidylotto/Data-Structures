# Rewrite the queue class using a stack.

class QueueWithStacks:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self, val):
        self.inbox.append(val)

    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        if self.outbox:
            return self.outbox.pop()
        else:
            print("Queue is empty!")

    def isEmpty(self):
        return not (self.inbox or self.outbox)

    def show(self):
        temp = self.outbox[::-1] + self.inbox
        print(f"Queue: {temp}")



# Test:

q = QueueWithStacks()
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
q.show()
print("Dequeued:", q.dequeue())
q.show()
