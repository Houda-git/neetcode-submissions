class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profits = []
        for i in range(n):
            for j in range(i+1, n):
                profit = prices[j] - prices[i]
                if profit >= 0:
                    profits.append(profit)
        return max(profits, default = 0)
