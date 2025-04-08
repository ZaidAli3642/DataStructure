class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        
        i = 1
        j = 1
        print(nums[j])
        while (j < len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i += 1
            j += 1

        return i
        
        
        
