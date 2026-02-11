# ---------------------------------------- Recursive Function ----------------------------------------

# Write the Recursive Factorial Function.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# Write the Recursive Multiplication Function.
def multiply(a,b):
    if b == 0:
        return 0
    return multiply(a,b-1) + a

# Write the Recursive Integer Division Function.
def divide(a,b):
    if a < b:
        return 0
    return divide(a-b,b) + 1

# Solve the Recursive Function below.
def test(a,b):
    if a < b:
        return a * b
    return test(a-1,b) + test(a-2,b) + test(a-3,b) + 5

# Solve the Recursive Function below.
def test(a,b):
    if a < b:
        return a * b
    return test(a-1,b) + test(a-2,b-1) + test(a-3,b-2) + 5