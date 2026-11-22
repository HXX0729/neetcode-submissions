class Solution:
    #和爬楼梯很像，多了个条件判断，如果i合法，如果i和i-1一起合法，分为两类，分别累加到结果
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]

