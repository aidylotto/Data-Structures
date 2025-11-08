# Design a new stack class that has 35 methods.

class SuperStack:
    def __init__(self):
        self.list = []

    def push(self, x): self.list.append(x)
    def pop(self): return self.list.pop() if self.list else None
    def peek(self): return self.list[-1] if self.list else None
    def size(self): return len(self.list)
    def isEmpty(self): return len(self.list) == 0
    def clear(self): self.list.clear()
    def reverse(self): self.list.reverse()
    def copy(self): return self.list.copy()
    def duplicate(self): self.list += self.list.copy()
    def sum(self): return sum(self.list)
    def avg(self): return sum(self.list)/len(self.list) if self.list else 0
    def max(self): return max(self.list)
    def min(self): return min(self.list)
    def search(self, x): return x in self.list
    def count(self, x): return self.list.count(x)
    def unique(self): self.list = list(set(self.list))
    def sort(self): self.list.sort()
    def sort_desc(self): self.list.sort(reverse=True)
    def push_many(self, lst): [self.push(x) for x in lst]
    def pop_many(self, n): [self.pop() for _ in range(n)]
    def get_all(self): return self.list
    def replace(self, old, new): self.list = [new if x == old else x for x in self.list]
    def remove(self, x): self.list.remove(x)
    def even_only(self): self.list = [x for x in self.list if x % 2 == 0]
    def odd_only(self): self.list = [x for x in self.list if x % 2 != 0]
    def top_two_sum(self): return self.list[-1]+self.list[-2]
    def top(self): return self.list[-1]
    def bottom(self): return self.list[0]
    def median(self): import statistics; return statistics.median(self.list)
    def mode(self): import statistics; return statistics.mode(self.list)
    def range(self): return max(self.list)-min(self.list)
    def top_index(self): return len(self.list)-1
    def clone(self): import copy; return copy.deepcopy(self)
    def shuffle(self): import random; random.shuffle(self.list)



# Test:

s = SuperStack()
s.push_many([1, 2, 3, 4, 5])
print(s.avg(), s.sum(), s.max(), s.min())
s.reverse()
s.show = print(s.get_all())
