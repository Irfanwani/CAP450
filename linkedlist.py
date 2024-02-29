class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            return
        
        current = self.head
        while(current.next):
            current = current.next
        
        current.next = newNode


    def display(self):
        current = self.head
        while(current):
            print(current.val)
            current = current.next



ll = LinkedList()

for i in range(10):
    ll.append(i)

ll.display()

