from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        m: number of elements in nums1
        n: number of elements in nums2
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        m = m
        n = n
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m]
                m -= 1
            else:
                nums1[last] = nums2[n]
                n -= 1
            last -= 1
        
        while n > 0:
            nums1[last] = nums2[n]
            n, last = n - 1, last - 1
        print(nums1)

s = Solution()
# s.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
# s.merge([0], 0, [1], 1)
# s.merge([1], 1, [], 0)
s.merge([4,5,6,0,0,0],3,[1,2,3],3)
