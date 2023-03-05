# 121. 买卖股票的最佳时机
# best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # DP
        minprice = prices[0]
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit
    
prices = [1]
print(Solution().maxProfit(prices))