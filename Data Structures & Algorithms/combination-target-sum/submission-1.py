class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtracking(path, start, target):
            if target == 0:
                result.append(path.copy())
                return
            if target < 0:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(path, i, target - nums[i])
                path.pop()

        backtracking([], 0, target)
        return result
