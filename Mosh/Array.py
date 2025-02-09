
class Array:
    def __init__(self, length):
        self.length = length
        self.size = 0
        self.array = [None] * length

    def insert(self, value):

        self.check_size_and_copy()
        self.array[self.size] = value
        self.size = self.size + 1

    def check_size_and_copy(self):
        if self.size != self.length - 1:
            return
        
        self.length *= 2
        new_array = [self.array[i] if i < self.size else None for i in range(self.length)]
        
        self.array = new_array

    def remove_at(self, index):
        if index < 0 or index > self.size:
            return -1

        removed_element = self.array[index]
        self.array[index] = None

        for i in range(index, self.size):
            self.array[i] = self.array[i + 1]
        
        self.size -= 1

        return removed_element

    def print(self):
        for index in range(0, self.size):
            print(self.array[index])

array = Array(3)
array.insert(10)
array.insert(20)
array.insert(30)
array.insert(40)
array.remove_at(1)
array.print()