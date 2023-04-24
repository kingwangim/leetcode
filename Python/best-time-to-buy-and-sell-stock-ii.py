class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)-1):
            v = prices[i+1] - prices[i]
            if v > 0:
                ans += v
        return ans
