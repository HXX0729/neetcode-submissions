"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #想想把所有起点和终点映射在同一根数轴上，起点是绿色，终点是红色，每次路过绿色count++,红色count--。count就是此时有多少个会议在同时进行
        events = []
        res = 0
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))
        count = 0
        events.sort(key = lambda x: (x[0], x[1]))
        for e in events:
            count += e[1]
            res = max(res, count)
        return res