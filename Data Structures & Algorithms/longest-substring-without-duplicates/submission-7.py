class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l, r = 0, 0
        window = set()
        length = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
                length -= 1
            window.add(s[r])
            length += 1
            ans = max(ans, length)
        return ans
