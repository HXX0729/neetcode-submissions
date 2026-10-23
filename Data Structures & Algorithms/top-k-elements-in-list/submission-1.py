class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        bucket = [ [] for _ in range(n+1) ]
        for num, freq in count.items():
            bucket[freq].append(num)

        ans = []
        
        for j in range(n, 0, -1):
            for n in bucket[j]:
                if len(ans) == k:
                    return ans
                ans.append(n)

        return ans

        
