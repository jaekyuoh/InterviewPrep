class Solution:
    def maxProfitBF(self, prices: list[int]) -> int:
        l = len(prices)
        maxPr = 0
        for i in range(l):
            for j in range(i, l):
                val = prices[j] - prices[i]
                if maxPr < val:
                    maxPr = val
        return maxPr
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res