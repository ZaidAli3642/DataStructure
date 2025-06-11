class MinStack:
    def __init__(self, capacity) -> None:
        self.items = [None] * capacity
        self.min_stack = [None] * capacity
        self.size = capacity