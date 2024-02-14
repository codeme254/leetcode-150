# code author - Dennis Otwoma (github - codeme254)
# logic/algorithm from neetcode: https://www.youtube.com/watch?v=ZI2z5pq0TqA

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        finds the maximum amount of rainwater that can be trapped
        Args:
            heights: an array of elevations
        Returns:
            the maximum amount of rainwater that can be trapped
        """
        if len(height) == 0:
            return 0
        # at h[i], the amount of water that can be trapped there is:
        # min(max_left_of_h, max_right_of_h) - h[i]

        # find all the maximums to the left of each h[i] and store them in an array
        max_lefts = []
        current_max_left = height[0]
        for h in height:
            if current_max_left >= h:
                max_lefts.append(current_max_left)
            else:
                current_max_left = h
                max_lefts.append(current_max_left)
        
        # find all the maximums to the right of each h[i] and store them in an array
        max_rights = []
        current_max_right = height[len(height)-1]
        i = len(height)-1
        while i >= 0:
            if current_max_right >= height[i]:
                max_rights.append(current_max_right)
            else:
                current_max_right = height[i]
                max_rights.append(current_max_right)
            i -= 1
        # reversing the max_rights since we started from the end
        max_rights.reverse()

        total_trapped = 0
        for i in range(0, len(height)):
            current_trapped = min(max_lefts[i], max_rights[i]) - height[i]
            if current_trapped > 0:
                total_trapped += current_trapped
        return total_trapped


s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([]))