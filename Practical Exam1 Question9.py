# Add a method to the stack that prioritizes it.

import heapq

class PriorityStack:
    def __init__(self):
        self.list = []

    def push(self, value, priority):
        heapq.heappush(self.list, (priority, value))

    def pop(self):
        if self.list:
            return heapq.heappop(self.list)[1]

    def show(self):
        print(f"Priority Stack: {self.list}")



# Test:

ps = PriorityStack()
ps.push("A", 3)
ps.push("B", 1)
ps.push("C", 2)
ps.show()
print("Popped:", ps.pop())
ps.show()
