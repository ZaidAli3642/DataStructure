from collections import defaultdict

class MostFrequenet:

    def most_frequent(self, items: list):
        map = defaultdict(int)
        
        for value in items:
            map[value] = map.get(value, 0) + 1
        
        MAX = -1
        result = items[0]
        for key in map:
            if map[key] > MAX:
                MAX = map[key]
                result = key
            
        
        return result



input = [1, 2, 2, 3, 3, 3,3, 4]
most_frequent = MostFrequenet()
print(most_frequent.most_frequent(input))