class node:
    def _init_(self, data):
        self.data = data
        self.next = None
        self.prev = None
class linkedlist:
    def _init_(self):
        self.head = None
        self.tail = None
    def insert(self, data):
        newnode = node(data)
        self.tail = newnode
        if self.head is None:
            self.head = newnode
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=newnode
            newnode.prev=current
    def display_f(self):
        current = self.head
        while current:
            print(current.data,end="->")
            current = current.next
        print("\n")
    def display_b(self):
        current = self.tail
        while current:
            print(current.data,end="<-")
            current = current.prev

obj=linkedlist()
obj.insert(5)
obj.insert(6)
obj.insert(3)
obj.display_f()
obj.display_b()