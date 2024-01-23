from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen_numbers = {}
        i = 0
        j = 0 # pointer for replacement
        while i < len(nums):
            if seen_numbers.get(nums[i]):
                i += 1
            else:
                seen_numbers[nums[i]] = True
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j += 1
        return j
s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(s.removeDuplicates([1, 1, 2]))
print(s.removeDuplicates([0, 0]))
print(s.removeDuplicates([]))