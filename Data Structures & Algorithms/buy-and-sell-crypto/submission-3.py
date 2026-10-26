class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        left_min = prices[0]
        for i in range(n):
            left_min = min(left_min, prices[i])
            ans = max(ans, prices[i] - left_min)
        return ans
