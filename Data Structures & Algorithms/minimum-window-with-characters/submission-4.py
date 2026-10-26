class Solution:
    

    def minWindow(self, s: str, t: str) -> str:
        def outnumbers(window_s, window_t):
            for i in range(128):
                if window_s[i] < window_t[i]:
                    return False
            return True

        ns = len(s)
        nt = len(t)
        l, r = 0, 0
        window_s = [0] * 128
        window_t = [0] * 128
        have = 0
        need = nt
        ans = []
        best = (0,ns+1)
        #print("hi")
        for i in range(nt):
            window_t[ ord(t[i]) ] += 1
        

        for r in range(ns):

            if window_s[ ord(s[r]) ] < window_t[ ord(s[r]) ]:
                have += 1
            window_s[ ord(s[r]) ] += 1
            
            while have == need:
                best = (l, r) if (r-l)<(best[1]-best[0]) else best

                if window_s[ ord(s[l]) ] == window_t[ ord(s[l]) ]:
                    have -= 1
                window_s[ ord(s[l]) ] -= 1

                l = l + 1
    
        if best == (0,ns+1):
            return ""
        else:
            return s[best[0] : best[1] + 1]










