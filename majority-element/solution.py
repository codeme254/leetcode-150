from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency_counter = {}
        for num in nums:
            if not frequency_counter.get(num):
                frequency_counter[num] = 1
            else:
                frequency_counter[num] += 1
        for key, value in frequency_counter.items():
            if value > len(nums)/2:
                return key

s = Solution()
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))