class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 1e99
        profit = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < buy:
                buy = prices[i - 1]
            if prices[i] - buy > 0 and prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
            
            