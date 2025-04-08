class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        # Now sort only the first `i` elements (in-place)
        nums[:i] = sorted(nums[:i])
        return i
    
# Test cases
solution = Solution()
nums4 = [0,0,3,2,2,1,4,2]
val4 = 2
k4 = solution.removeElement(nums4, val4)
print(f"Test 4: k={k4}, nums={nums4[:k4]}")  # Expected: k=5, nums=[0,0,1,3,4]

