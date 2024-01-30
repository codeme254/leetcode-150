from typing import List
class Solution:
    def canReachTarget(self, nums: List, left_idx: int, right_idx: int):
        """
        checks whether a number at a given left index can help move
        to a right index

        Args:
            nums: the list containing the elements
            left_idx: the left index pointing the left target number
            right_idx: the right index pointing the goal
        Returns:
            true if the number at left_idx is enough steps to move to
            the number at right_idx, otherwise false
        """
        steps_remaining = right_idx - left_idx
        return nums[left_idx] >= steps_remaining

    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        current = len(nums)-2
        goal = len(nums)-1

        while current >= 0:
            if self.canReachTarget(nums, current, goal):
                goal = current
            current -= 1
        # print(goal)
        return goal == 0
s = Solution()

print(s.canJump([3,2,1,0,4]))
# print(s.canJump([3]))
print(s.canJump([1, 0, 3]))
print(s.canJump([2, 0, 3]))
print(s.canJump([1,2,0,1]))