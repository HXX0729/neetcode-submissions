"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
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