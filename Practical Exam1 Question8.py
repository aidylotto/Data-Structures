# Add a method to the circular queue that converts it to a simple queue.

class CircularQueue:
    def __init__(self, size=5):
        self.list = [None]*size
        self.front = -1
        self.rear = -1
        self.size = size

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full!")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.list[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty!")
            return
        val = self.list[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return val

    def get_valid_data(self):
        if self.front == -1:
            return []
        data = []
        i = self.front
        while True:
            data.append(self.list[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        return data

    # New Method
    def to_linear_queue(self):
        data = self.get_valid_data()
        new_list = [None]*self.size
        for i, val in enumerate(data):
            new_list[i] = val
        self.list = new_list
        self.front = 0 if data else -1
        self.rear = len(data) - 1 if data else -1
        print(f"Converted to linear queue: {self.list}")



# Test:

cq = CircularQueue(5)
cq.enqueue('A')
cq.enqueue('B')
cq.enqueue('C')
cq.dequeue()
cq.enqueue('D')
cq.enqueue('E')
cq.enqueue('F')
cq.to_linear_queue()
