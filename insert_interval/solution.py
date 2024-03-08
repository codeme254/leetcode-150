from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Inserts newInterval into intervals such that intervals 
        is still sorted in ascending order by starti and intervals 
        still does not have any overlapping intervals

        Args:
          intervals: main sorted interval
          newInterval: interval to be inserted into intervals
        
        Return:
          intervals after insertion without any overlapping intervals
        """
        if len(intervals) == 0:
            return [newInterval]
        
        intervals.append(newInterval)
        intervals = sorted(intervals)
        result = []
        
        current_merge = intervals[0]
        for i in range(1, len(intervals)):
            if current_merge[1] >= intervals[i][0]:
                current_merge[1] = max(current_merge[1], intervals[i][1])
            else:
                result.append(current_merge)
                current_merge = intervals[i]
        if current_merge:
            result.append(current_merge)
        return result

s = Solution()
print(s.insert([],[4, 5]))
print(s.insert([[1,3],[6,9]],[2, 5]))
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4, 8]))