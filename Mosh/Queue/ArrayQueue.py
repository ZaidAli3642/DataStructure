

class ArrayQueue:
    def __init__(self, capacity) -> None:
        self.items = [None] * capacity
        self.size = capacity
        self.count = -0
        self.rear = -0
        self.front = -0

    def enqueue(self, value):
        if self.is_full():
            raise Exception("Queue is full")
        
        self.items[self.rear] = value
        self.count += 1
        self.rear = (self.rear + 1) % self.size

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        item = self.items[self.front]
        self.items[self.front] = None
        self.front += (self.front + 1) % self.size
        self.count -= 1

        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        return self.items[self.rear - 1]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def print(self):
        return self.items

array_queue = ArrayQueue(5)
array_queue.enqueue(1)
array_queue.enqueue(2)
array_queue.enqueue(3)
array_queue.enqueue(4)
array_queue.enqueue(5)
array_queue.dequeue()
array_queue.dequeue()
print(array_queue.print())