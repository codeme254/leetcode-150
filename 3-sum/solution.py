# Solution from neetcode : https://youtu.be/jzZsG8n2R9A
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds three numbers that add upto zero

        Args:
          nums: a list of numbers to find the numbers from
        
        Returns:
          A list of lists wher each nested list contains three unique triplets
          that add upto zero
        """
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l, r = i + 1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

s = Solution()

# print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([-2,0,0,2,2]))
# print(s.threeSum([0, 0, 0]))
# print(s.threeSum([0, 1, 1]))