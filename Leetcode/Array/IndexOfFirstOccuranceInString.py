'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        haystack_len = len(haystack)
        needle_len = len(needle)

        if haystack_len < needle_len:
            return -1
        
        for i in range(haystack_len - needle_len + 1):
            found = True
            for j in range(needle_len):
                if needle[j] != haystack[i + j]:
                    found = False
                    break
            
            if found:
                return i
        
        return -1

        
        

# first solution:

# check if haystack and needle are not equal then return -1
# if they are equal or haystack length is greater then:
#       loop over the haystack using while and compare the entire needle string with haystack according to the needle length\
#       step: 1
#              sad = 3, so first three characters haystack

#             i
haystack = "mississipipi"
#               j
needle = "issipi"


print(Solution().strStr(haystack=haystack, needle=needle))