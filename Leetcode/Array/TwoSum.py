class Solution:
    def twoSum(self, nums, target: int):
        
        seen = {}

        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target - nums[i]], i] 
            
            seen[nums[i]] = i
        

            
solution = Solution()

# Test case 1: Basic case
nums1 = [2, 7, 11, 15]
target1 = 9
print(f"Input: nums = {nums1}, target = {target1}")
print(f"Output: {solution.twoSum(nums1, target1)}\n")

# Test case 2: Same numbers
nums2 = [3, 3]
target2 = 6
print(f"Input: nums = {nums2}, target = {target2}")
print(f"Output: {solution.twoSum(nums2, target2)}\n")

# Test case 3: Negative numbers
nums3 = [-1, -2, -3, -4, -5]
target3 = -8
print(f"Input: nums = {nums3}, target = {target3}")
print(f"Output: {solution.twoSum(nums3, target3)}\n")

