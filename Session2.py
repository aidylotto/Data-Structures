# Stack

class stack:
    def __init__(self,limit):
        self.stack = []
        self.limit = limit
        
    # Push Method
    def push(self,x):
        if len(self.stack) >= (self.limit):     # Exception Case (Stack Being Full)
            print("Stack is full!")
            return -1
        self.stack.append(x)
        
    # Pop Method
    def pop(self):
        if len(self.stack) == 0:     # Exception Case (Stack Being Empty)
            print("Stack is empty.")
            return -1
        return self.stack.pop()
    
    # Peek Method
    def peek(self):
        if len(self.stack) == 0:     # Exception Case (Stack Being Empty)
            print("Stack is empty.")
            return -1
        return self.stack[-1]
    
    # Find Method
    def find(self,x):
        for i in range(len(self.stack)):
            if self.stack[i] == x:
                print(f"Found at index: {i}")
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i] == x:
                print(f"The last index that contains {x}: {i}")
                break

    # Replace Method
    def replace(self,x,y):
        for i in range(len(self.stack)):
            if self.stack[i] == x:
                self.stack[i] = y        