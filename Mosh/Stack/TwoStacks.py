class TwoStacks:
    def __init__(self, capacity) -> None:
        self.items = [None] * capacity
        self.top1 = -1
        self.top2 = capacity
        self.size = capacity
    
    def push1(self, value):
        if self.is_full1():
            return

        self.top1 += 1
        self.items[self.top1] = value

    def push2(self, value):
        if self.is_full2():
            return
        
        self.top2 -= 1
        self.items[self.top2] = value

    def pop1(self):
        if self.is_empty1():
            return
        
        self.items[self.top1] = None
        self.top1 -= 1

    def pop2(self):
        if self.is_empty2():
            return
        
        self.items[self.top2] = None
        self.top2 += 1
    
    def is_empty1(self) -> bool:
        return self.top1 == -1

    def is_empty2(self) -> bool:
        return self.top2 == self.size

    def is_full1(self) -> bool:
        return self.top1 + 1 == self.top2
    
    def is_full2(self) -> bool:
        return self.top2 - 1 == self.top1

    def print(self):
        return self.items
    
two_stacks = TwoStacks(5)
two_stacks.push1(1)
two_stacks.push1(2)
two_stacks.push2(5)
two_stacks.push2(4)
two_stacks.push2(3)
print(two_stacks.print())