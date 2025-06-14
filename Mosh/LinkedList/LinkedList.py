class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.count = 0
    
    def add_last(self, item):
        node = Node(item)

        if self.first is None:
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node

        self.count += 1

    def add_first(self, item):
        node = Node(item)

        if self.first is None:
            self.first = self.last = node
        else:
            node.next = self.first
            self.first = node

        self.count += 1

    def remove_last(self):
        # if list is empty

        if self.first is None:
            raise Exception('LinkedList is empty')

        # if list only has one node
        if self.first == self.last:
            self.first = self.last = None

        else:
            currnet = self.first
            prev = None
            while currnet.next is not None:
                prev = currnet
                currnet = currnet.next
            
            prev.next = None
            self.last = prev
            
        self.count -= 1

    def remove_first(self):
        if self.first is None:
            raise Exception('LinkedList is empty')

        # if list only has one node
        if self.first == self.last:
            self.first = self.last = None
        
        else:
            temp = self.first.next
            self.first.next = None
            self.first = temp
        
        self.count -= 1

    def insert_at(self, index, item):
        if index < 0 or index >= self.count:
            raise Exception("Invalid index")
        
        node = Node(item)

        if index == 0:
            self.add_first(item)
        else:
            current = self.first
            prev = None
            i = 0

            while current is not None:
                if  i == index:
                    break
                prev = current
                current = current.next
                i += 1

            prev.next = node
            node.next = current
            self.count += 1


    def remove_at(self, index):
        if index < 0 or index >= self.count:
            raise Exception("Invalid index")
        
        if index == 0:
            self.remove_first()
        elif index == self.count:
            self.remove_last()
        else:
            current = self.first
            prev = None
            i = 0
            while current is not None:
                if index == i:
                    break

                i += 1
                prev = current
                current = current.next
            #    p     c 
            #   [10 -> 30]
            prev.next = current.next
            current.next = None
            self.count -= 1

    def index_of(self, item):
        
        if self.first is None:
            raise Exception("LinkedList is empty.")
        
        current = self.first
        i = 0
        while current is not None:
            if current.value == item:
                return i
            i += 1
            current = current.next
        
        return -1
    
    def exists(self, item):
        if self.first is None:
            raise Exception("LinkedList is empty.")
        
        current = self.first
        while current is not None:
            if current.value == item:
                return True
            current = current.next
        
        return False

    def print(self):
        current = self.first

        while current is not None:
            print(current.value)
            current = current.next

    def get_kth_from_end(self, k):
        slow = self.first
        fast = self.first

        for _ in range(k):
            fast = fast.next
        
        while fast is not None:
            fast = fast.next
            slow = slow.next

        return slow.value
    
    def reverse(self):
        current = self.first
        prev = None

        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        self.last = self.first
        self.first = prev

    def print_middle(self):
        #        s      f
        # [10 -> 20 -> 30]

        fast = self.first
        slow = self.first

        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        if fast.next is not None:
            print(f"{slow.value}, {slow.next.value}")
        else:
            print(slow.value)

    @staticmethod
    def create_with_loop():
        list = LinkedList()

        list.add_last(10)
        list.add_last(20)
        list.add_last(30)

        node = list.last

        list.add_last(40)
        list.add_last(50)

        list.last.next = node

        return list
    
    def has_loop(self):
        list = self.create_with_loop()

        slow = list.first
        fast = list.first.next

        while fast is not None:
            if slow == fast:
                return True

            fast = fast.next.next
            slow = slow.next
        
        return False


