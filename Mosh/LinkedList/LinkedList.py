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
    
    @staticmethod
    def createWithLoop():
        list = LinkedList()

        list.add_last(10)
        list.add_last(20)
        list.add_last(30)

        node = list.last

        list.add_last(40)
        list.add_last(50)

        list.last.next = node  # type: ignore

        return list

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

    def get_kth_from_the_end(self, k: int):
        
        fast = self.first
        slow = self.first
        i = 1
        for _ in range(k):
            if fast is None:
                return -1
            fast = fast.next
        
        while fast is not None:
            if slow is None:
                return -1

            fast = fast.next
            slow = slow.next


        return slow.value if slow is not None else -1

    def printMiddle(self):
        slow = self.first
        fast = self.first

        while fast != self.last and fast != None and fast.next != self.last:
            fast = fast.next.next if fast.next is not None else None
            slow = slow.next if slow is not None else None

        if fast == self.last:
            print(slow.value if slow is not None else None)
        else:
            if slow is not None and slow.next is not None:
                print(f"{slow.value},{slow.next.value}")

    def hasLoop(self):
        
        slow = self.first
        fast = self.first
        while fast is not None:
            fast = fast.next.next if fast.next is not None else None
            slow = slow.next if slow is not None else None

            if slow == fast:
                return True
        
        return False

    def insert_at(self, index: int, item: int):
        if self.first is not None and (index < 0 or index > self.length() - 1):
            return
        
        if self.first == None:
            self.add_last(item)
            return
    
        node = Node(item)

        previous = None
        current = self.first
        currentIndex = 0
        while current is not None:
            if currentIndex == index:
                break

            previous = current
            current = current.next
            currentIndex += 1
        

        if previous is not None:
            previous.next = node
        node.next = current
        self.size += 1
        if self.first == current:
            self.first = node

    
    def remove_at(self, index: int):
        if index < 0 or index > self.length() - 1:
            return

        if self.first is None:
            return
        
        previous = None
        current = self.first
        currentIndex = 0
        while current is not None:
            if currentIndex == index:
                break

            previous = current
            current = current.next
            currentIndex += 1
        

        # if index == 0
        if self.first == current and current is not None:
            if self.first == self.last:
                self.first, self.last = None, None
                self.size -= 1
                return
            
            self.first = current.next
            current.next = None
            self.size -= 1
            return
        
        if previous is not None:
            previous.next = current.next if current is not None else None
        if current is not None:
            current.next = None
        self.size -= 1

        


# list = LinkedList.createWithLoop()
# print(list.hasLoop())


linkedList = LinkedList()

linkedList.add_last(10)
linkedList.add_last(20)
linkedList.add_last(30)
linkedList.add_last(40)

linkedList.remove_at(3)

linkedList.print()
# print(linkedList.length())
