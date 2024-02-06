from typing import List
class Solution:
    def canMakeCompleteCircuit(self, i: int, gas: List[int], cost: List[int]) -> bool:
        """
        checks whether starting from gas station i will make a complete circuit
        Args:
            i: gas station at hand
            gas: gas stations
            cost: costs
        Returns:
            true if we can make a complete circuit from gas station i
        """
        k = i
        current_gas_level = gas[i]
        keep_moving = True
        while keep_moving:
            if current_gas_level < cost[i]:
                return False
            current_gas_cost = cost[i]
            i += 1
            if i >= len(gas):
                i = 0
            # if i is equivalent to k, it means we have made a complete circuit
            if i == k:
                return True
            current_gas_level = current_gas_level - current_gas_cost + gas[i]
            
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 1 and gas[0] > cost[0]:
            return 0
        if len(gas) == 1 and gas[0] < cost[0]:
            return -1
        for i in range(0, len(gas)):
            if self.canMakeCompleteCircuit(i, gas, cost):
                return i
        return -1

s = Solution()
# print(s.canMakeCompleteCircuit(0,[1,2,3,4,5],[3,4,5,1,2]))
print(s.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
# print(s.canCompleteCircuit([2,3,4], [3,4,3]))
# print(s.canCompleteCircuit([3], [2]))
print(s.canMakeCompleteCircuit(0, [5,1,2,3,4],[4,4,1,5,1]))
print(s.canCompleteCircuit([5,1,2,3,4],[4,4,1,5,1]))