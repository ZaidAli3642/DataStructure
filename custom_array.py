


class Array:
    def __init__(self, length):
        self.length = length
        self.items = [0] * length
        self.size = 0
    
    def insert(self, item):
        self.resizeItems()
        self.items[self.size] = item
        self.size += 1

    def resizeItems(self):
        if self.size != self.length:
            return
        
        new_length = self.length * 2
        new_array = [None] * new_length

        for i in range(self.size):
            new_array[i] = self.items[i]
        
        self.length = new_length
        self.items = new_array
    

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid index")

        for i in range(index, self.size - 1):
            self.items[i] = self.items[i + 1]
        
        self.items[self.size - 1] = 0
        self.size -= 1


    def index_of(self, item):
        for i in range(self.size):
            if item == self.items[i]:
                return i
            
        return -1

    def print(self):
        for i in range(self.size):
            print(self.items[i])

    # 
    #   Exercise 1:
    #  *     Extend the Array class and add a new method to return the largest number.
    #  *     What is the runtime complexity of this method?
    #  */
    # runtime complexity will be O(n)
    def max(self):
        if self.size <= 0:
            return -1

        LARGEST_NUM = self.items[0]
        for i in range(self.size):
            if self.items[i] is not None and self.items[i] > LARGEST_NUM:
                LARGEST_NUM = self.items[i]

        return LARGEST_NUM

    #  * Exercise 2:
    #  *     Extend the Array class and add a method to return the common items in this array
    #  *     and another array.

    # Runtime complexity O(n * m)
    #   Where n is the size of other
    #   And m is the size self.items

    def intersect(self, other):
        if not isinstance(other, list):
            return []

        intersection = [0] * self.size
        intersection_size = 0

        for item in other:
            if self.index_of(item) != -1 and item not in intersection:
                intersection[intersection_size] = item
                intersection_size += 1
        
        return intersection[:intersection_size]
    

    # RUNTIME COMPLEXITY O(n + m):
    #   WHERE n is the size of self.items
    #   AND m is the size of other
    #   AND k is negligible because it will always less than n and m so k <= min(n, m)

    def intersect2(self, other):
        if not isinstance(other, list):
            return []
        
        self_dic = {}

        for item in self.items: # O(n)
            self_dic[item] = True
        
        intersection = [0] * self.size
        intersection_size = 0

        seen = {}

        for item in other: # O(m)
            if item not in seen and item in self_dic:
                intersection[intersection_size] = item
                intersection_size += 1
                seen[item] = True

        return intersection[:intersection_size] # O(k)



    # * Exercise 3:
    #  *     Extend the Array class and add a method to reverse the array.
    #  *     For example, if the array includes [1, 2, 3, 4], after reversing and printing it,
    #  *     we should see [4, 3, 2, 1].

    # Runtime complexity will be O(n)

    def reverse(self):
        new_items = [0] * self.size

        for i in range(self.size):
            new_items[i] = self.items[self.size - 1 - i]
        
        self.items = new_items;


    #  * Exercise 4:
    #  *     Extend the Array class and add a new method to insert an item at a given index:
    #  *     public void insertAt(int item, int index)
    #  RUNTIME COMPLEXITY O(n)

    def insert_at(self, index, item):
        if index < 0 or index > self.size:
            raise ValueError("Index out of bounds")
        
        self.resizeItems()
        for i in range(self.size, -1, -1):
            if index <= i:
                self.items[i + 1] = self.items[i]
        
        self.items[index] = item
        self.size += 1
        