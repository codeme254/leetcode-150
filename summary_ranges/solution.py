from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        creates the smallest sorted list of ranges that cover all 
        the numbers in an array exactly.

        Args:
          nums: input array of numbers
        
        Returns: the smallest sorted list of ranges that cover all 
        the numbers in an array exactly.
        """
        if len(nums) == 0:
            return nums
        if len(nums) == 1:
            return [str(nums[0])]
        
        result = []
        current_range = []
        previous = nums[0]
        current_range.append(previous)

        for i in range(1, len(nums)):
            if nums[i]-1 == previous:
                current_range.append(nums[i])
                previous = nums[i]
            else:
                if len(current_range) == 1:
                    result.append(str(current_range[0]))
                else:
                    first = current_range[0]
                    last = current_range[len(current_range)-1]
                    rng = str(first)+"->"+str(last)
                    result.append(rng)
                previous = nums[i]
                current_range = []
                current_range.append(previous)
        if len(current_range) == 1:
            result.append(str(current_range[0]))
        elif len(current_range) > 1:
            first = current_range[0]
            last = current_range[len(current_range)-1]
            rng = str(first)+"->"+str(last)
            result.append(rng)
        return result

s = Solution()
print(s.summaryRanges([]))
print(s.summaryRanges([2]))
print(s.summaryRanges([0,1,2,4,5,7,8,9]))
print(s.summaryRanges([0,2,3,4,6,8,9]))