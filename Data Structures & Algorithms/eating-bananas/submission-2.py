class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def min_h(piles, k):
            sum = 0
            for p in piles:
                sum += (p + k - 1) // k
            return sum
        
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            if h >= min_h(piles, mid):
                r = mid - 1
            else: 
                l = mid + 1
            
        return l
