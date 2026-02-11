# ---------------------------------------- Singly Linked List ----------------------------------------

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Singly_Linked_List():
    def __init__(self):
        self.head = None

    # Delete First Method
    def del_first(self):
        if self.head is None:     # Exception Case: List is empty
            print("List is empty!")
            return
        c = self.head
        self.head = c.next
        del c

    # Delete Last Method
    def del_last(self):
        if self.head is None:     # Exception Case: List is empty
            print("List is empty!")
            return
        if self.head.next is None:     # Exception Case: List has only one member
            self.del_first()
        else:
            c = self.head
            while c.next.next:
                c = c.next
            del c.next
            c.next = None

    # Delete After Method
    def del_after(self,x):
        if self.head is None:     # Exception Case: List is empty
            print("List is empty!")
            return
        if self.head.next is None:     # Exception Case: List has only one member
            print("List has only one member.")
            return
        c = self.head
        while c.next:
            if c.data == x:
                if c.next is None:     # Exception Case: x is last node
                    print("No node after x!")
                    return
                a = c.next
                c.next = c.next.next
                del a
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
        if self.head.next is None:     # Exception Case: List has only one member
            print("List has only one member!")
            return
        if self.head.next.data == x:     # Exception Case: X is second node
            self.del_first()
            return
        if self.head.next.next is None:     # Exception Case: List has only two members
            print("x not found!")
            return
        c = self.head
        while c.next.next:
            if c.next.next.data == x:
                a = c.next
                c.next = a.next
                del a
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
        if self.head.next is None:     # Exception Case: List has only one member
            print("x not found!")
            return
        c = self.head
        while c.next:
            if c.next.data == x:
                a = c.next
                c.next = a.next
                del a
                return
            c = c.next
        print("x not found!")

    # Delete All Method
    def del_all(self):
        if self.head is None:     # Exception Case: List already empty
            print("List is empty!")
            return
        while self.head:
            a = self.head
            self.head = a.next
            del a
