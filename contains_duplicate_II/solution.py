from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        checks whether there are two distinct indices i and j in the array
        such that nums[i] == nums[j] and abs(i - j) <= k.

        Args:
          nums: input array
          k: target value k
        
        Returns:
          true if there are two distinct indices i and j in the array
          such that nums[i] == nums[j] and abs(i - j) <= k, false otherwise
        """

        previous_numbers = {}
        for i in range(0, len(nums)):
            if nums[i] in previous_numbers:
                previous_idx = previous_numbers[nums[i]]
                result = abs(previous_idx-i)
                if result <= k:
                    return True
                else:
                    previous_numbers[nums[i]] = i
            else:
                previous_numbers[nums[i]] = i
        return False

s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1], 3))
print(s.containsNearbyDuplicate([1,0,1,1], 1))
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))
print(s.containsNearbyDuplicate([1,1], 2))