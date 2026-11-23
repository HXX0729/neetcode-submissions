class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(len(s)+1):
            idx = i - 1
            for word in wordDict:
                if dp[i] == 1:
                    break
                length = len(word)
                if idx-length+1 >=0 and s[idx-length+1: idx+1] == word:
                    dp[i] = dp[i - length]
        return True if dp[len(s)]==1 else False