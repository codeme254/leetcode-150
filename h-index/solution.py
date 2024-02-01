from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
    
        for i, citation in enumerate(citations, 1):
            if citation >= i:
                h = i
            else:
                break
    
        return h
        

s = Solution()
print(s.hIndex([3,0,6,1,5]))
print(s.hIndex([1,3,1]))
# print(s.hIndex([11, 15]))