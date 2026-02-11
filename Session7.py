# ---------------------------------------- Doubly Linked List ----------------------------------------

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_Linked_List():
    def __init__(self):
        self.head = None

    # Insert First Method
    def insert_first(self,x):
        if self.head is None:     # Exception Case: List is empty
            self.head = Node(x)
            return
        a = Node(x)
        a.next = self.head
        self.head.prev = a
        self.head = a

    # Insert Last Method
    def insert_last(self,x):
        if self.head is None:     # Exception Case: List is empty
            self.head = Node(x)
            return
        a = Node(x)
        c = self.head
        while c.next:
            c = c.next
        c.next = a
        a.prev = c

    # Insert After Method
    def insert_after(self,x,y):
        if self.head is None:     # Exception Case: List is empty
            print("List is empty!")
            return
        c = self.head
        while c:
            if c.data == x:
                if c.next:
                    a = Node(y)
                    a.next = c.next
                    c.next.prev = a
                    c.next = a
                    a.prev = c
                    return
            c = c.next
        print("x not found!")

    # Insert Before Method
    def insert_before(self,x,y):
        if self.head is None:     # Exception Case: List is empty
            print("List is empty!")
            return
        if self.head.data == x:     # Exception Case: x is first node
            self.insert_first(y)
            return
        c = self.head
        while c:
            if c.data == x:
                a = Node(y)
                a.prev = c.prev
                a.next = c
                c.prev.next = a
                c.prev = a
                return
            c = c.next
        print("x not found!")

    # Delete First Method
    def del_first(self):
        if self.head is None:     # Exception Case: List is empty
            print("List is empty!")
            return
        c = self.head
        self.head = self.head.next
        del c
        if self.head:
            self.head.prev = None

    # Delete Last Method
    def del_last(self):
        if self.head is None:     # Exception Case: List is empty
            print("List is empty!")
            return
        if self.head.next is None:     # Exception Case: List has only one member
            self.del_first()
            return
        c = self.head
        while c.next:
            c = c.next
        c.prev.next = None
        del c

     # Delete After Method
    def del_after(self,x):
        if self.head is None:     # Exception Case: List is empty
            print("List is empty!")
            return
        c = self.head
        while c:
            if c.data == x:
                if c.next:     # Exception Case: x is last node
                    a = c.next
                    c.next = c.next.next
                    if c.next:
                        c.next.prev = c
                    del a
                    return
                print("x is lost!")
                return
            c = c.next
        print("x not found!")

    # Delete Before Method
    def del_before(self,x):
        if self.head is None:     # Exception Case: List is empty
            print("List is empty!")
            return
        if self.head.data == x:     # Exception Case: X is first node
            print("No node before x!")
            return
        c = self.head
        while c:
            if c.data == x:
                if c.prev:
                    a = c.prev
                    c.prev = a.prev
                    if c.prev:
                        c.prev.next = c
                    del a
                    return
                print("x is first.")
                return
            c = c.next
        print("x not found!")

    # Delete X Method
    def del_x(self,x):
        if self.head is None:     # Exception Case: List is empty
            print("List is empty!")
            return
        if self.head.data == x:     # Exception Case: x is first node
            self.del_first()
            return
        c = self.head
        while c:
            if c.data == x:
                if c.next is None:     # Exception Case: x is last node
                    self.del_last()
                    return
                c.prev.next = c.next
                c.next.prev = c.prev
                del c
                return
            c = c.next
        print("x not found!")

    # Delete All Method
    def del_all(self):
        while self.head:
            self.del_first()
