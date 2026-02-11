# ---------------------------------------- Singly Linked List ----------------------------------------

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Singly_Linked_List():
    def __init__(self):
        self.head = None

    # Insert First Method
    def insert_first(self,x):
        if self.head is None:     # Exception Case: List is empty
            self.head = Node(x)
        else:
            a = Node(x)
            a.next = self.head
            self.head = a

    # Insert Last Method
    def insert_last(self,x):
        if self.head is None:     # Exception Case: List is empty
            self.head = Node(x)
        else:
            a = Node(x)
            c = self.head
            while c.next:
                c = c.next
            c.next = a

    # Insert After Method
    def inser_after(self,x,y):
        if self.head is None:     # Exception Case: List is empty
            print("List is empty!")
        else:
            c = self.head
            while c:
                if c.data == x:
                    a = Node(y)
                    a.next = c.next
                    c.next = a
                    return
                c = c.next
            print("x not found!")

    # Insert Before Method
    def insert_before(self,x,y):
        if self.head is None:     # Exception Case: List is empty
            print("List is empty!")
            return
        if self.head.data == x:     # Exception Case: x is at head
            if self.head.next is None:
                self.insert_first(y)
            return
        c = self.head
        while c.next:
            if c.next.data == x:
                a = Node(y)
                a.next = c.next
                c.next = a
                return
            c = c.next
        print("x not found!")