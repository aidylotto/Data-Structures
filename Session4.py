# I don't know what this session's about!

class queue:
    def __init__(self,max = 10):
        self.list = [] * max
        self.front = -1
        self.rear = -1
        
    # Delete Method    
    def delete(self):
        if self.front == -1:     # Exception Case (Queue being empty)
            print("Queue is empty.")
            return
        if self.front == self.rear:     # Exception Case (Having only one member in the queue)
            k = self.list[self.rear]
            self.rear = -1
            self.front = -1
            return k
        k = self.list[self.front]
        self.front += 1
        return k
    
    # Is-Full Method
    def is_full(self):
        return (self.rear +1) % len(self.list) == self.front
    
    # Is-Empty Method
    def is_empty(self):
        return self.front == -1
    
    # Show-Valid Method
    def show_valid(self):
        if self.rear >= self.front:
            for i in range(self.front,(self.rear +1),1):
                print(self.list[i])
        else:
            for i in range(self.front,len(self.list),1):
                print(self.list[i])
            for i in range(self.rear +1):
                print(self.lit[i])
        # Or:
        # i = self.front
        # print(self.list[i])
        # while i != self.rear:
        #     i = (i +1) % len(self.list)
        #     print(self.list[i])
                
    # Show-Invalid Method
    def show_invalid(self):
        if self.rear >= self.front:
            for i in range((self.rear +1), len(self.list), 1):
                print(self.list[i])
            for i in range(self.front):
                print(self.lit[i])
        else:
            for i in range((self.rear +1),self.front,1):
                print(self.list[i])
        # Or:
        # i = (self.rear +1) % len(self.list)
        # while i != self.front:
        #     print(self.list[i])
        #     i = (i +1) % len(self.list)
        
    # Find Method
    def find(self, x):
        if len(self.list) == 0:
            print("List is empty!")
            return -1
        for i in range(len(self.list)):
            if self.list[i] == x:
                print("Value found at index:", i)
                return i
        print("Value not found!")
        return -1

    # Replace Method
    def replace(self, x, y):
        if len(self.list) == 0:
            print("List is empty!")
            return
        for i in range(len(self.list)):
            if self.list[i] == x:
                self.list[i] = y
                print("Value replaced successfully.")
                return
        print("Value not found!")
