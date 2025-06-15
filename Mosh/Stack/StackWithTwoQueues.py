from queue import Queue

class StackWithTwoQueues:
    def __init__(self) -> None:
        self.queue1 = Queue()
        self.queue2 = Queue()
    
    def push(self, item):
        self.queue1.put(item)

        while not self.queue2.empty():
            self.queue1.put(self.queue2.get())
        
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if self.queue2.empty():
            raise Exception("Queue is empty")
        
        return self.queue2.get()
    
stack_with_two_queues = StackWithTwoQueues()
stack_with_two_queues.enqueue(10)
stack_with_two_queues.enqueue(20)
stack_with_two_queues.enqueue(30)

print(stack_with_two_queues.queue1.queue)
print(stack_with_two_queues.queue2.queue)