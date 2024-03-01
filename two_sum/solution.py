from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        finds two integers that add upto a given target given a list of
        integers

        Args:
          nums: a list of integers
          target: target sum
        
        Returns:
          a list with two elements where each element represents an index
          of an integer that is part of the two numbers
        """

        lookup = {}

        for i in range(0, len(nums)):
            remainder = target - nums[i]
            if remainder in lookup:
                return [lookup[remainder], i]
            lookup[nums[i]] = i

s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3], 6))