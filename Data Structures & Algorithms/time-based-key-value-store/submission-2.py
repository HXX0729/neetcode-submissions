class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        t = (timestamp, value)
        self.d[key].append(t)

    def get(self, key: str, timestamp: int) -> str:
        line = self.d[key]
        l, r = 0, len(line) - 1
        while l <= r:
            mid = (l + r) // 2
            if timestamp < line[mid][0]:
                r = mid - 1
            elif timestamp > line[mid][0]:
                l = mid + 1
            elif timestamp == line[mid][0]:
                return line[mid][1]
        return line[r][1] if r != -1 else ""
        
                
