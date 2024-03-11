from typing import List
# Solution from Timoth H Chang: https://www.youtube.com/watch?v=_WIFehFkkig
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        finds the minimum number of arrows required to burst all balloons
        on an imaginary xy plane

        Args:
          points: list of x coordinates that balloons extend from and to
        
        Returns:
          The minimum number of arrows required to shoot all those balloons
        """
        if not points:
            return 0
        points.sort()
        prev = points[0]
        total = 1
        for s, e in points[1:]:
            if s > prev[1]:
                total += 1
                prev = [s, e]
            else:
                prev[1] = min(prev[1], e)
        return total