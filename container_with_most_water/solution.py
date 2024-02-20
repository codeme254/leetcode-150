from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Finds the amount of water the biggest container will hold

        Args:
          height: a list of heights
        
        Returns:
          the amount of water that the biggest container will hold
        """
        i = 0
        j = len(height)-1
        current_max = -1

        while i < j:
            current_amount = (j - i) * min(height[j], height[i])
            current_max = max(current_max, current_amount)
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
        return current_max

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))