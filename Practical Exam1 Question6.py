# Write a function that first creates a thousand circular queue objects and a thousand stack objects, then stores the valid data of the queues in reverse order on the stacks.

class Stack:
    def __init__(self):
        self.list = []
    def push(self, item):
        self.list.append(item)

class CircularQueue:
    def __init__(self, size=5):
        self.list = [None]*size
        self.front = -1
        self.rear = -1
        self.size = size

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.list[self.rear] = item

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


def transfer_data():
    queues = [CircularQueue() for _ in range(1000)]
    stacks = [Stack() for _ in range(1000)]

    # Filling queues with hypothetical data
    for i, q in enumerate(queues):
        q.enqueue(i)
        q.enqueue(i + 1000)

    # Reverse data transfer
    for i in range(1000):
        data = queues[i].get_valid_data()
        for val in reversed(data):
            stacks[i].push(val)

    print("Data transfer completed successfully.")



# Test:

transfer_data()
