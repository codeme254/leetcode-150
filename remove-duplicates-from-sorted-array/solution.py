from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen_numbers = {}
        unique_elements = []
        for number in nums:
            if seen_numbers.get(number):
                continue
            unique_elements.append(number)
            seen_numbers[number] = True
        
        for i in range(0, len(unique_elements)):
            nums[i] = unique_elements[i]
        k = len(unique_elements)
        unique_elements.clear()
        print(nums)
        return k

s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(s.removeDuplicates([1, 1, 2]))
print(s.removeDuplicates([0, 0]))
print(s.removeDuplicates([]))