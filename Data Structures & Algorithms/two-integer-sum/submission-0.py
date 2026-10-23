class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}
        for i in range(n):
            num = nums[i]
            if target - num in seen:
                return[seen[target - num], i]
            seen[num] = i
        return []