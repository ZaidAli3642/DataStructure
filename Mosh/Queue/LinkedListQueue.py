from typing import Optional


class Node:
    value: int
    def __init__(self, value) -> None:
        self.value = value
        self.next: Optional["Node"] = None


class LinkedListQueue:
    def __init__(self) -> None:
        self.first: Optional[Node] = None
        self.last: Optional[Node] = None
        self.count = 0

    def enqueue(self, value):
        node = Node(value)

        if self.first == None:
            self.first = self.last = node
        else:
            assert self.last is not None
            self.last.next = node
            self.last = node

        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        item = self.first
        if self.first == self.last:
            self.first = self.last = None
        else:
            assert self.first is not None
            self.first = self.first.next
        
        self.count -= 1

        return item.value if item is not None else None

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        return self.first.value if self.first is not None else None
        

    def size(self):
        return self.count

    def is_empty(self):
        return self.first is None

    def print(self):
        current = self.first

        while current is not None:
            print(current.value)
            current = current.next

linked_list_queue = LinkedListQueue()
linked_list_queue.enqueue(10)
linked_list_queue.enqueue(20)
linked_list_queue.enqueue(30)
linked_list_queue.print()