class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            profit = max(profit, price - min_price)
            if price < min_price:
                min_price = price

        return profit