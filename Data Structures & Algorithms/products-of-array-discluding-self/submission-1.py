class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right= [0] * n
        res = [0] * n
        left_prod = 1
        right_prod = 1
        for i in range(n):
            left_prod *= nums[i]
            left[i] = left_prod
        for j in range(n-1, -1, -1):
            right_prod *= nums[j]
            right[j] = right_prod

        for k in range(1, n-1):
            res[k] = left[k-1] * right[k+1]
        res[0] = right[1]
        res[n-1] = left[n-2]
        return res
