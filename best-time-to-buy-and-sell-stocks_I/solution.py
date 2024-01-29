from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0
        
        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
                sell += 1
            else:
                current_profit = prices[sell] - prices[buy]
                max_profit = max(current_profit, max_profit)
                sell += 1
        return max_profit
        