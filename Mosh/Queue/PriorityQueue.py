# so there are two ways.
# 1. Consider the highest value as priority. 
#    enqueue the values based on ordering O(n) time complexity 
#    pop the last element as

# 2. Consider the lowest value as priority.
#    enqueue the values based on ordering O(n) time complexity or enqueue the values O(1) without ordering
#    dequeue the values from (first index) or (specific index) and shift the elements to left



class PriorityQueue:
    def __init__(self, capacity) -> None:
        self.items = [None] * capacity
        self.count = 0
        self.size = capacity

    def enqueue(self, item):
        # considering first approach
        if self.count == self.size:
            raise Exception("Queue is full")

        i = self.count

        for j in range(self.count - 1, -1, -1):
            if self.items[j] > item:
                self.items[j + 1] = self.items[j]
                i = j
            else:
                break

        self.items[i] = item
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise Exception("Queue is empty!")
        
        self.count -= 1
        item = self.items[self.count]
        self.items[self.count] = None

        return item

    def print(self):
        return self.items
    
priority_queue = PriorityQueue(5)
priority_queue.enqueue(10)
priority_queue.enqueue(30)
priority_queue.enqueue(40)
priority_queue.enqueue(20)
priority_queue.enqueue(50)
priority_queue.dequeue()
print(priority_queue.print())
