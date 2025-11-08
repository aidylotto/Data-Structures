# Write a function to turn postfix examples into infix using stack structure.

class Stack:
    def __init__(self):
        self.list = []
    
    def isEmpty(self):
        return len(self.list) == 0
    
    def push(self,x):
        self.list.append(x)
    
    def pop(self):
        if not self.isEmpty():
            return self.list.pop()
    
    def peek(self):
        if not self.isEmpty():
            return self.list[-1]


def postfix_to_infix(y):
    stack = Stack()
    operators = "+,-,*,/,^,%,=,<,>"


    for i in y.split():
        if i not in operators:
            stack.push(i)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            new_expr = "(" + op1 + i + op2 + ")"
            stack.push(new_expr)

    return stack.pop()

exp = "A B + C *"
print(postfix_to_infix(exp))
exp2 = "A B C * + D /"
print(postfix_to_infix(exp2))