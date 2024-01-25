from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return 0
        if len(nums) == 1:
            return 1
        frequency = {}
        for i in range(0, len(nums)):
            if not frequency.get(nums[i]):
                frequency[nums[i]] = 1
            elif frequency.get(nums[i]) == 1:
                frequency[nums[i]] += 1
            elif frequency.get(nums[i]) == 2:
                # loop until we find something valid to be here
                j = i
                while nums[j] == nums[i] or frequency.get(nums[j]) == 2:
                    j += 1
                    if j >= len(nums):
                        print(nums, frequency)
                        return i
                if j < len(nums):
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    if not frequency.get(nums[i]):
                        frequency[nums[i]] = 1
                    else:
                        frequency[nums[i]] += 1

s = Solution()
# s.removeDuplicates([0,0,0,0,0,0,1,1,1,1,2,3,3])
# s.removeDuplicates([0, 0, 0])
print(s.removeDuplicates([1,1,1,2,2,3]))
print(s.removeDuplicates([0,0,1,1,1,1,2,3,3]))
print(s.removeDuplicates([0]))