class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 如果x-1在，那么x就不是起点
        s = set(nums)
        res = 0
        for x in nums:
            if x - 1 not in s:
                count = 1
                while x + 1 in s:
                    count += 1
                    x += 1
                res = max(res, count)
        return res