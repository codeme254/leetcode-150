from typing import List
# solution from neetcode https://youtu.be/aYqYMIqZx5s
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Finds the minimal length of a subarray whose sum is greater than
        or equal to target

        Args:
          target: target sum
          nums: a list of positive integer numbers
        
        Returns:
          length of a subarray whose sum is greater than or equal to target
          or 0 if such a subarray doesn't exist in nums
        """
        left, total = 0, 0
        result = float('inf')
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                result = min(right-left+1, result)
                total -= nums[left]
                left += 1
        return 0 if result == float('inf') else result

s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
print(s.minSubArrayLen(7, [2,3,1,2,4,7]))