class ContainsDuplicate:
    def contains_duplicate(self, items):
        numbers = set()

        for value in items:
            if value in numbers:
                return True
            numbers.add(value)
        
        return False

items = [1,2,3,3]
contains_duplicate = ContainsDuplicate()
print(contains_duplicate.contains_duplicate(items))



