from typing import List
# solution from neetcode: https://www.youtube.com/watch?v=P6RZZMu_maU
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        finds the length of the longest consecutive elements sequence

        Args:
          nums: unsorted array of integers
        
        Returns:
          the length of the longest consecutive elements sequence
        """

        if len(nums) == 1:
            return 1
        
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))