# Add a method to the circular queue that reports the last five times the queue has been full.

import datetime

class CircularQueueWithTime:
    def __init__(self, size):
        self.list = [None]*size
        self.front = -1
        self.rear = -1
        self.size = size
        self.full_times = []

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full!")
            t = datetime.datetime.now().strftime("%H:%M:%S")
            self.full_times.append(t)
            if len(self.full_times) > 5:
                self.full_times.pop(0)
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.list[self.rear] = item

    def show_last_five_full(self):
        print(f"Last 5 full times: {self.full_times}")



# Test:

q = CircularQueueWithTime(2)
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
q.enqueue('D')
q.enqueue('E')
q.show_last_five_full()
