# Add a method to the circular queue that reports the last 5 logs.

class CircularQueue:
    def __init__(self, size):
        self.list = [None]*size
        self.front = -1
        self.rear = -1
        self.size = size
        self.logs = []

    def log(self, action):
        self.logs.append(action)
        if len(self.logs) > 5:
            self.logs.pop(0)

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
            self.log("enqueue failed")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.list[self.rear] = item
            self.log(f"enqueue({item})")

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
            self.log("dequeue failed")
        else:
            val = self.list[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            self.log(f"dequeue({val})")

    def show_logs(self):
        print("Last 5 logs:", self.logs)



# Test:

cq = CircularQueue(3)
cq.enqueue('A')
cq.enqueue('B')
cq.enqueue('C')
cq.dequeue()
cq.enqueue('D')
cq.show_logs()
