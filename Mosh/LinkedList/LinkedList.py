class Node:
    value: int
    next: 'Node | None'
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None 

class LinkedList:
    def __init__(self) -> None:
        self.first: Node | None = None
        self.last: Node | None = None
        self.size = 0

    def add_last(self, item: int) -> None:
        node = Node(item)     
        if self.first == None:
            self.first = self.last = node
        else:
            if self.last:
                self.last.next = node
                self.last = node
        self.size += 1
    
    def add_first(self, item: int) -> None:
        node = Node(item)

        if self.first == None:
            self.first = self.last = node
        else:
            node.next = self.first
            self.first = node
        
        self.size += 1
    
    def index_of(self, item: int) -> int:

        current = self.first
        index = -1
        
        while current != None:
            index += 1
            if current.value == item:
                return index
            current = current.next
        
        return index
    
    def contains(self, item: int) -> bool:
        
        current = self.first
        found = False

        while current != None:
            if current.value == item:
                found = True
                break
            current = current.next
        
        return found
    
    def remove_first(self):

        if self.first == None:
            return
        
        if self.first == self.last:
            self.first = self.last = None
        else:
            if self.first:
                self.first = self.first.next
        self.size -= 1
    
    def remove_last(self):
        if self.first == None:
            return
            
        if self.first == self.last:
            self.first = self.last = None
        else:            
            current = self.first
            
            while current.next != None and current.next.next != None:
                current = current.next
                
            self.last = current
            current.next = None
        
        self.size -= 1

    def print(self):
        current = self.first

        while current != None:
            print(current.value)
            current = current.next
    
    def length(self):
        return self.size

    def reverse(self):
        prev = None
        current = self.first
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        self.last = self.first
        self.first = prev


linkedList = LinkedList()


# linkedList.add_last(10)
# linkedList.add_last(20)
# linkedList.add_last(30)
linkedList.reverse()
linkedList.print()