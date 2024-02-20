from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Finds two numbers from a list of numbers that add up to a given target

        Args:
          numbers: a list of integer numbers
          target: the target sum
        
        Returns:
          A list of two elements which are index+1 of the two numbers that add
          upto the given target
        """
        i = 0
        j = len(numbers)-1

        while i < j:
            current_sum = numbers[i]+numbers[j]
            if current_sum == target:
                return [i+1, j+1]
            if current_sum > target:
                j -= 1
            elif current_sum < target:
                i += 1

s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([2,3,4], 6))
print(s.twoSum([-1, 0], -1))
print(s.twoSum([5, 25, 75], 100))