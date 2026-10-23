class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        pairs = sorted(count.items(), key = lambda x: x[1], reverse = True)
        ans = []
        for i in range(k):
            ans.append(pairs[i][0])
        return ans