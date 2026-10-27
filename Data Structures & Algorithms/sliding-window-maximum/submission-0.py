class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range(k-1):
            new = nums[i]
            while q and new >= nums[q[-1]]:
                q.pop()
            q.append(i)
    
        for r in range( k-1, len(nums) ):
            l = r - k + 1
            new = nums[r]
            while q and new >= nums[q[-1]]:
                q.pop()
            q.append(r)

            #out of date
            while q and q[0] < l:
                q.popleft()

            # the old man must have sth strong
            res.append(nums[q[0]])

        return res
            
            