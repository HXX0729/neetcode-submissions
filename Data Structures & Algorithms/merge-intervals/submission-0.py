class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        cur = intervals[0]
        for i in range(1, len(intervals) ):
            if cur[1] < intervals[i][0]:
                res.append(cur)
                cur = intervals[i]
            else:
                cur = [cur[0], max(cur[1], intervals[i][1])]
        res.append(cur)
        return res