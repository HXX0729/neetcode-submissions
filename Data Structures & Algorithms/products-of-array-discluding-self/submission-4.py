class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n

        res = [0] * n
        right_prod = 1
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        for j in range(n-2, -1, -1):
            right_prod *= nums[j+1]
            left[j] *= right_prod
        
        return left
