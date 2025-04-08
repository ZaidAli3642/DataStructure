"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
    Input: nums = [3,2,3]
    Output: 3

Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

Constraints:
    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        thresh_hold = int(len(nums) / 2)
        
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
            
            if seen[num] > thresh_hold:
                return num
                
        return -1
    


# Using the Boyer-Moore Voting Algorithm to implement the O(1) space
#
# The Boyer-Moore Voting Algorithm is used to find the majority element in O(1) space:
# 1. Initialize a candidate element and a counter set to 0
# 2. For each element in array:
#    - If counter is 0, set current element as the candidate
#    - If current element matches candidate, increment counter
#    - If current element differs from candidate, decrement counter
# 3. The final candidate will be the majority element
#
# This works because:
# - Majority element appears more than n/2 times
# - When counter reaches 0, we effectively "cancel out" equal numbers of majority and minority elements
# - Since majority element appears more times, it will always be the final candidate


class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate

print(Solution2().majorityElement(nums=[2,2,1,1,1,2,2]))