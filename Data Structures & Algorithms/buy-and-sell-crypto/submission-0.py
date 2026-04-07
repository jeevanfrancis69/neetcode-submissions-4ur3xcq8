class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1,len(prices)):
                profit = prices[j] - prices[i]

                if profit < 0:
                    profit = 0

                maxProfit = max(maxProfit, profit)

        return maxProfit
        