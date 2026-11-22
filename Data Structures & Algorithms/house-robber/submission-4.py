class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #dp[n] = 截止到第n间，最多能抢多少钱，不一定要抢第n间
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2,len(nums)):
            #最后一间不抢，或最后一间抢，这两种分支
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[len(nums) - 1]