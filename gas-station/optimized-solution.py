"""Solution by neetcode: https://www.youtube.com/watch?v=lJwbPZGo05A"""
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i]-cost[i])
            if total < 0:
                total = 0
                start = i + 1
        return start