class TwoSum:
    @staticmethod
    def two_sum(nums, target):
        num_map = {}

        for index, value in enumerate(nums):
            complement = (target - value)
            if complement in num_map:
                return [num_map[complement], index]
            
            num_map[value] = index

nums = [3,4,5,6]
target = 7

print(TwoSum.two_sum(nums, target))