# Write a 3D Linked List class with 15 methods.

class Node3D():
    def __init__(self,data):
        self.data = data
        self.next_x = None
        self.next_y = None
        self.next_z = None


class Linked_List_3D():
    def __init__(self):
        self.head = None

    # 1 Insert X
    def insert_x(self,x):
        if self.head is None:
            self.head = Node3D(x)
        else:
            a = Node3D(x)
            a.next_x = self.head
            self.head = a

    # 2 Insert Y
    def insert_y(self,x,y):
        c = self.search(x)
        if c:
            c.next_y = Node3D(y)

    # 3 Insert Z
    def insert_z(self,x,z):
        c = self.search(x)
        if c:
            c.next_z = Node3D(z)

    # 4 Delete X
    def del_x(self):
        if self.head:
            a = self.head
            self.head = a.next_x
            del a

    # 5 Delete Y
    def del_y(self,x):
        c = self.search(x)
        if c:
            c.next_y = None

    # 6 Delete Z
    def del_z(self,x):
        c = self.search(x)
        if c:
            c.next_z = None

    # 7 Search
    def search(self,x):
        c = self.head
        while c:
            if c.data == x:
                return c
            c = c.next_x
        return None

    # 8 Show X
    def show_x(self):
        c = self.head
        while c:
            print(c.data)
            c = c.next_x

    # 9 Show Y
    def show_y(self,x):
        c = self.search(x)
        if c and c.next_y:
            print(c.next_y.data)

    # 10 Show Z
    def show_z(self,x):
        c = self.search(x)
        if c and c.next_z:
            print(c.next_z.data)

    # 11 Count
    def count(self):
        c = self.head
        counter = 0
        while c:
            counter += 1
            c = c.next_x
        return counter

    # 12 Is Empty
    def is_empty(self):
        return self.head is None

    # 13 Delete All
    def del_all(self):
        while self.head:
            self.del_x()

    # 14 Update
    def update(self,x,new):
        c = self.search(x)
        if c:
            c.data = new

    # 15 Get Head
    def get_head(self):
        return self.head