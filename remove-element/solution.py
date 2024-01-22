from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        removes an elment from a list in place
        """
        replace_ptr = len(nums) - 1
        if len(nums) == 0:
            return 0
        while nums[replace_ptr] == val:
            replace_ptr -= 1
            if replace_ptr < 0:
                nums = []
                return len(nums)
        
        i = 0
        while i <= replace_ptr:
            if nums[i] == val:
                temp = nums[i]
                nums[i] = nums[replace_ptr]
                nums[replace_ptr] = temp
                while nums[replace_ptr] == val:
                    replace_ptr -= 1
            i += 1
        return i

s = Solution()
print(s.removeElement([7], 7))
print(s.removeElement([3, 2, 3, 1, 2, 2, 5], 2))
print(s.removeElement([0,1,2,2,3,0,4,2], 2))
print(s.removeElement([3,2,2,3], 3))
print(s.removeElement([], 3))