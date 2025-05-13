class Stack:
    def __init__(self, size) -> None:
        self.stack = [None] * size
        self.count = 0
        self.size = size
    
    def expand_stack(self):
        if self.count != self.size:
            return
        
        new_size = self.size * 2
        new_stack = [None] * new_size

        for index in range(self.count):
            new_stack[index] = self.stack[index]
        
        self.stack = new_stack
        self.size = new_size

    def push(self, item):
        self.expand_stack()

        self.stack[self.count] = item
        self.count += 1
    
    def pop(self):
        if self.count == 0:
            return

        self.count -= 1
        self.stack[self.count] = None
    
    def peek(self):
        if self.count == 0:
            return -1
        
        return self.stack[self.count - 1]
    
    def is_empty(self):
        return self.count == 0

stack = Stack(3)

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack.is_empty())
