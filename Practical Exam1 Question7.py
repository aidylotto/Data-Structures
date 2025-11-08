# Write a new class that can create a priority circular queue class that has at least 10 methods by inheriting from the two circular queue and stack classes.

import heapq
from datetime import datetime

class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if self.list:
            return self.list.pop()

    def peek(self):
        if self.list:
            return self.items[-1]

    def isEmpty(self):
        return len(self.list) == 0


class CircularQueue:
    def __init__(self, size=5):
        self.list = [None]*size
        self.front = -1
        self.rear = -1
        self.size = size

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full!")
            return False
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.list[self.rear] = item
        return True

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty!")
            return None
        value = self.list[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return value


# Hybrid class with double inheritance
class PriorityCircularQueue(Stack, CircularQueue):
    def __init__(self, size=5):
        Stack.__init__(self)
        CircularQueue.__init__(self, size)
        self.heap = []  # Heap data structure for priority

    def enqueue_with_priority(self, value, priority):
        heapq.heappush(self.heap, (priority, value))

    def dequeue_priority(self):
        if not self.heap:
            print("Queue is Empty!")
            return None
        return heapq.heappop(self.heap)[1]

    def show_heap(self):
        print(f"Priority Queue: {self.heap}")

    def peek_priority(self):
        if self.heap:
            return self.heap[0][1]

    def isEmpty(self):
        return len(self.heap) == 0

    def size_heap(self):
        return len(self.heap)

    def clear(self):
        self.heap.clear()

    def change_priority(self, old, new_priority):
        temp = [(p, v) for p, v in self.heap if v != old]
        heapq.heapify(temp)
        heapq.heappush(temp, (new_priority, old))
        self.heap = temp

    def log_enqueue(self, val):
        print(datetime.now(), f"Enqueued: {val}")



# Test:

pq = PriorityCircularQueue()
pq.enqueue_with_priority("A", 3)
pq.enqueue_with_priority("B", 1)
pq.enqueue_with_priority("C", 2)
pq.show_heap()
print(f"Dequeued: {pq.dequeue_priority()}")
pq.show_heap()
