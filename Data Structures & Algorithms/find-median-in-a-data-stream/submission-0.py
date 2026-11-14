class MedianFinder:

    def __init__(self):
        self.l_h = []
        self.r_h = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.l_h, -num)
        heapq.heappush(self.r_h, -heapq.heappop(self.l_h))
        if(len(self.r_h) > len(self.l_h)):
            heapq.heappush(self.l_h, -heapq.heappop(self.r_h))
        return 
        

    def findMedian(self) -> float:
        if(len(self.l_h) == len(self.r_h)):
            return (-self.l_h[0] + self.r_h[0]) / 2
        else:
            return -self.l_h[0]
        