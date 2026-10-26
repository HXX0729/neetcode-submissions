class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                ans = max(ans, prices[j] - prices[i])
        return ans