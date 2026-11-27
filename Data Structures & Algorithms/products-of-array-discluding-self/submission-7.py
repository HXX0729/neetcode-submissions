class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums))
        postfix = [1] * (len(nums))
        prefix[0] = nums[0]
        postfix[len(nums)-1] = nums[len(nums) - 1]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]

        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]

        res = [0] * (len(nums))
        for i in range(len(nums)):
            left = prefix[i-1] if i-1>=0 else 1
            right = postfix[i+1] if i+1<len(nums) else 1
            res[i] = left * right

        return res
