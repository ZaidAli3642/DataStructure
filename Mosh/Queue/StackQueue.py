class QueueUsingStacks:
    def __init__(self):
        self.stack1 = [] 
        self.stack2 = [] 

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("Queue is empty")
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("Queue is empty")
        return self.stack2[-1]

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def __len__(self):
        return len(self.stack1) + len(self.stack2)

    def __repr__(self):
        if not self.stack2:
            return f"Queue: {self.stack1}"
        else:
            # Show elements in correct queue order
            combined = self.stack2[::-1] + self.stack1
            return f"Queue: {combined}"

stack_queue = QueueUsingStacks()
stack_queue.enqueue(10)
stack_queue.enqueue(20)
stack_queue.enqueue(30)
print(stack_queue.peek())