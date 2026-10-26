class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0, 0
        window = defaultdict(int)
        ans = 0

        for r in range(len(s)):
            window[s[r]] += 1
            while ((r - l + 1) - max(window.values())) > k:
                window[s[l]] -= 1
                l += 1
                
            ans = max(ans, (r - l + 1) )
        
        return ans