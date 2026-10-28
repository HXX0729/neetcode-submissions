class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        arrival_time = [(0,0)] * n
        s = []
        for i in range(n):
            arrival_time[i] = [position[i], (target - position[i]) / speed[i]]
        arrival_time.sort(key = lambda x: x[0] , reverse = True)

        for i in range(len(arrival_time)):
            pair = arrival_time[i]
            if i != 0 and pair[1] < s[-1][1]:
                pair[1] = s[-1][1]
            s.append(pair)
        
        res = set()
        for pair in s:
            res.add(pair[1])
        return len(res)


            
                
