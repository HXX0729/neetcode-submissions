class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 1
        intervals.sort(key = lambda x: x[1])
        print(intervals)
        prev_end = intervals[0][1]
        for i in range(len(intervals)):
            if intervals[i][0] >= prev_end:
                count += 1
                prev_end = intervals[i][1]
        return len(intervals) - count
