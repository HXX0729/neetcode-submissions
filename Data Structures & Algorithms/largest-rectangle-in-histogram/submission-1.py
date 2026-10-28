class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        NSE_l = [n] * n
        NSE_r = [-1] * n
        s_l = []
        s_r = []
        #scan from left to right to fill out NSE_l
        for i in range(n):
            while s_l and heights[i] < heights[s_l[-1]]:
                idx = s_l.pop()
                NSE_l[idx] = i
            s_l.append(i)
        
        #scan from right to left to fill out NSE_l
        for i in range(n-1, -1, -1):
            while s_r and heights[i] < heights[s_r[-1]]:
                idx = s_r.pop()
                NSE_r[idx] = i
            s_r.append(i)
        
        res = 0
        for i in range(n):
            area = (NSE_l[i] - NSE_r[i] - 1) * heights[i]
            res = max(res, area)

        return res