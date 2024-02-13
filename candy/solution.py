# solution from neetcodeio https://www.youtube.com/watch?v=1IzCRCcK17A
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candys = [1]*len(ratings)

        # first pass left to right
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                candys[i] = candys[i-1]+1
        # second pass, right to left
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candys[i] = max(candys[i], candys[i+1]+1)
        return sum(candys)
s = Solution()
print(s.candy([3, 6, 1]))
print(s.candy([1,2,2]))
print(s.candy([1,0,2]))