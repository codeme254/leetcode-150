from typing import List

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

        if len(nums) == 1:
            if nums[0] == target:
                return 1
            else:
                return 0
        if sum(nums) < target:
            return 0
        
        min_size = float('inf')
        for i in range(0, len(nums)-1):
            if nums[i] >= target:
                return 1
            j = i + 1
            current_sum = nums[i]
            while j < len(nums):
                if nums[j] >= target:
                    return 1
                current_sum += nums[j]
                if current_sum >= target:
                    current_min_size = (j-i)+1
                    min_size = min(min_size, current_min_size)
                    break
                else:
                    j += 1
        return min_size

s = Solution()
print(s.minSubArrayLen(5, [5]))
print(s.minSubArrayLen(5, [4]))
print(s.minSubArrayLen(5, [4,1]))
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
print(s.minSubArrayLen(4, [1,4,4]))
print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))