# Design a new stack class that has 65 methods.

import random, statistics, copy

class UltraStack:
    def __init__(self):
        self.list = []

    # Basic Methods
    def push(self, x): self.list.append(x)
    def pop(self): return self.list.pop() if self.list else None
    def peek(self): return self.list[-1] if self.list else None
    def size(self): return len(self.list)
    def isEmpty(self): return len(self.list) == 0
    def clear(self): self.list.clear()
    def get_all(self): return self.list
    def copy(self): return self.list.copy()
    def reverse(self): self.list.reverse()

    # Numerical and statistical Methods
    def sum(self): return sum(self.list)
    def avg(self): return statistics.mean(self.list)
    def max(self): return max(self.list)
    def min(self): return min(self.list)
    def median(self): return statistics.median(self.list)
    def mode(self): return statistics.mode(self.list)
    def range(self): return max(self.list) - min(self.list)

    # Sorting Methods
    def sort(self): self.list.sort()
    def sort_desc(self): self.list.sort(reverse=True)
    def shuffle(self): random.shuffle(self.list)
    def unique(self): self.list = list(set(self.list))

    # Analytical Methods
    def count(self, x): return self.list.count(x)
    def search(self, x): return x in self.list
    def even_only(self): self.list = [x for x in self.list if x % 2 == 0]
    def odd_only(self): self.list = [x for x in self.list if x % 2 != 0]

    # Logical Methods
    def all_positive(self): return all(x > 0 for x in self.list)
    def all_negative(self): return all(x < 0 for x in self.list)
    def any_zero(self): return any(x == 0 for x in self.list)

    # String Methods
    def concat(self): return ''.join(map(str, self.list))
    def length_total(self): return sum(len(str(x)) for x in self.list)
    def upper_all(self): self.list = [str(x).upper() for x in self.list]
    def lower_all(self): self.list = [str(x).lower() for x in self.list]

    # Additive Methods
    def push_many(self, lst): [self.push(x) for x in lst]
    def pop_many(self, n): [self.pop() for _ in range(n)]
    def replace(self, old, new): self.list = [new if x == old else x for x in self.list]

    # Comparative Methods
    def equals(self, other): return self.list == other.list
    def greater_top(self, other): return self.peek() > other.peek()
    def smaller_top(self, other): return self.peek() < other.peek()

    # Advanced statistical Methods
    def variance(self): return statistics.variance(self.list)
    def stdev(self): return statistics.stdev(self.list)

    # Mathematical Methods
    def square_all(self): self.list = [x**2 for x in self.list]
    def sqrt_all(self): self.list = [x**0.5 for x in self.list]
    def add_constant(self, c): self.list = [x + c for x in self.list]
    def multiply_constant(self, c): self.list = [x * c for x in self.list]

    # Methods of working with memory
    def clone(self): return copy.deepcopy(self)
    def top_index(self): return len(self.list) - 1
    def bottom(self): return self.list[0] if self.list else None
    def top_two_sum(self): return self.list[-1] + self.list[-2]

    # Helper Methods
    def print_all(self): [print(x) for x in self.list]
    def remove(self, x): self.list.remove(x)
    def slice(self, start, end): return self.list[start:end]
    def insert_at(self, i, val): self.list.insert(i, val)
    def swap(self, i, j): self.list[i], self.list[j] = self.list[j], self.list[i]
    def reverse_half(self): mid = len(self.list)//2; self.list[:mid] = reversed(self.list[:mid])

    # Special Methods
    def palindrome(self): return self.list == self.list[::-1]
    def duplicate(self): self.list += self.list.copy()
    def clear_top_half(self): mid = len(self.list)//2; self.list = self.list[:mid]
    def rotate_right(self): self.list.insert(0, self.list.pop())
    def rotate_left(self): self.list.append(self.list.pop(0))
    def total_digits(self): return sum(len(str(abs(x))) for x in self.list)
    def abs_all(self): self.list = [abs(x) for x in self.list]
    def mod_all(self, m): self.list = [x % m for x in self.list]



# Test:

s = UltraStack()
s.push_many([1, 2, 3, 4, 5])
print("Sum:", s.sum(), "Avg:", s.avg())
s.reverse()
print("Reversed:", s.get_all())
s.square_all()
print("Squared:", s.get_all())
