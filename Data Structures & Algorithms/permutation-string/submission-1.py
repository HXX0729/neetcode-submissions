class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        if len(s2) < window_size:
            return False

        window1 = defaultdict(int)
        window2 = defaultdict(int)

        for idx in range(window_size):
            window1[s1[idx]] += 1
            window2[s2[idx]] += 1
        if window1 == window2:
            return True
        
        for r in range(window_size, len(s2)):
            window2[s2[r]] += 1
            window2[s2[r-window_size]] -= 1
            if window2[s2[r-window_size]] == 0:
                del window2[s2[r-window_size]]
            if window1 == window2:
                return True
        
        return False