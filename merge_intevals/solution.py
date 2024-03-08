from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merges all the overlapping intervals in a nested list

        Args:
          intervals: input nested list
        
        Returns:
          an array of the non-overlapping intervals that 
          covers all the intervals in the input.
        """
        if len(intervals) <= 1:
            return intervals
        
        intervals = sorted(intervals)
        current_merged = intervals[0]
        result = []
        for i in range(0, len(intervals)):
            if current_merged[1] >= intervals[i][0]:
                current_merged[1] = max(current_merged[1], intervals[i][1])
            else:
                result.append(current_merged)
                current_merged = intervals[i]
        if current_merged:
            result.append(current_merged)
        return result

s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
print(s.merge([[1,4],[0,2],[3,5],[7,9]]))
print(s.merge([[1,4],[4,5]]))