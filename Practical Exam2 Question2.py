# Write a 4D linked list class with 15 methods.

class Node4D():
    def __init__(self,data):
        self.data = data
        self.next_w = None
        self.next_x = None
        self.next_y = None
        self.next_z = None

class Linked_List_4D():
    def __init__(self):
        self.head = None

    # 1 Insert W
    def insert_w(self,x):
        if self.head is None:
            self.head = Node4D(x)
        else:
            a = Node4D(x)
            a.next_w = self.head
            self.head = a

    # 2 Insert X
    def insert_x(self,x,y):
        c = self.search(x)
        if c:
            c.next_x = Node4D(y)

    # 3 Insert Y
    def insert_y(self,x,y):
        c = self.search(x)
        if c:
            c.next_y = Node4D(y)

    # 4 Insert Z
    def insert_z(self,x,z):
        c = self.search(x)
        if c:
            c.next_z = Node4D(z)

    # 5 Delete W
    def del_w(self):
        if self.head:
            a = self.head
            self.head = a.next_w
            del a

    # 6 Delete X
    def del_x(self,x):
        c = self.search(x)
        if c:
            c.next_x = None

    # 7 Delete Y
    def del_y(self,x):
        c = self.search(x)
        if c:
            c.next_y = None

    # 8 Delete Z
    def del_z(self,x):
        c = self.search(x)
        if c:
            c.next_z = None

    # 9 Search
    def search(self,x):
        c = self.head
        while c:
            if c.data == x:
                return c
            c = c.next_w
        return None

    # 10 Show
    def show(self):
        c = self.head
        while c:
            print(c.data)
            c = c.next_w

    # 11 Count
    def count(self):
        c = self.head
        counter = 0
        while c:
            counter += 1
            c = c.next_w
        return counter

    # 12 Is Empty
    def is_empty(self):
        return self.head is None

    # 13 Update
    def update(self,x,new):
        c = self.search(x)
        if c:
            c.data = new

    # 14 Delete All
    def del_all(self):
        while self.head:
            self.del_w()

    # 15 Get Head
    def get_head(self):
        return self.head