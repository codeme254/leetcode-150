from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                max_profit += (prices[sell] - prices[buy])
            sell += 1
            buy += 1
        return max_profit

s = Solution()
print(s.maxProfit([1,2,3,4,5]))
print(s.maxProfit([7,6,4,3,1]))
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7]))