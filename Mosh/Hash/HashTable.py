class Node:
    def __init__(self, key, value) -> None:
        self.value = value
        self.key = key
        self.next = None
    
class HashTable:
    def __init__(self) -> None:
        self.items = [None] * 10

    def hash(self, key: int):
        return key % 10

    def put(self, key: int, value: str):
        index = self.hash(key)

        entry = self.items[index]
        
        current = entry
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        node = Node(key, value)
        node.next = entry # it can be None or a linked list and node will be added on start
        self.items[index] = node

    def remove(self, key: int):
        index = self.hash(key)
        entry = self.items[index]

        if entry is None:
            return entry

        current = entry
        prev = None
        while current is not None:
            if current.key == key:
                if prev:
                    prev.next = current.next
                    current.next = None
                else:
                    self.items[index] = None
                return
            
            prev = current 
            current = current.next

    def get(self,key: int):
        index = self.hash(key)

        entry = self.items[index]

        current = entry
        
        while current is not None:
            if current.key == key:
                break
            current = current.next

        return current.value if current is not None else None

hash_table = HashTable()
hash_table.put(5, "HI")
hash_table.put(6, "Hello")
hash_table.put(15, "New")
hash_table.put(5, "HIIIII")
hash_table.remove(25)
print(hash_table.get(25))