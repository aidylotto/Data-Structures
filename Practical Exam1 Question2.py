# Add a method to the stack that prioritizes the stack based on whether it's data is even or odd.

class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if self.list:
            return self.list.pop()

    def show(self):
        print(self.list)

    # New Method
    def prioritize_even(self):
        even = [x for x in self.list if x % 2 == 0]
        odd = [x for x in self.list if x % 2 != 0]
        self.list = even + odd



# Test:

s = Stack()
for n in [5, 2, 7, 4, 3, 8]:
    s.push(n)
s.prioritize_even()
s.show()
