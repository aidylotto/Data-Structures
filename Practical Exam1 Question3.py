# Add a method to the stack that every time it's called, If the stack is static, it will become dynamic, and if it is dynamic, it will become static.

class SmartStack:
    def __init__(self, size=5):
        self.list = []
        self.size = size
        self.dynamic = False

    def push(self, item):
        if len(self.list) < self.size or self.dynamic:
            self.list.append(item)
        else:
            print("Stack is Overflow")

    def toggle_mode(self):
        self.dynamic = not self.dynamic
        if self.dynamic:
            print("Stack changed to DYNAMIC")
        else:
            print("Stack changed to STATIC")



# Test:

s = SmartStack(3)
s.push(1)
s.push(2)
s.push(3)
s.push(4)          
s.toggle_mode()    
s.push(4)          
print(s.list)
