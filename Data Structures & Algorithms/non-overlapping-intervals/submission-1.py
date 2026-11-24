class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 按照终点排序，每次如果这个interval和prev_end冲突，就丢弃。思想是选择结束时间最少的，这样能给后面的人留出最多空间。题目问最少去掉几个就等价于最多同时保留几个。
        count = 1
        intervals.sort(key = lambda x: x[1])
        prev_end = intervals[0][1]
        for i in range(len(intervals)):
            if intervals[i][0] >= prev_end:
                count += 1
                prev_end = intervals[i][1]
        return len(intervals) - count
