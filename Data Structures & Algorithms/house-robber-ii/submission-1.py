class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums1 = nums[1:]
        nums2 = nums[:-1]

        #no rob 1:
        rob1, rob2 = 0, 0
        for x in nums1:
            new = max(rob1 + x, rob2)
            rob1, rob2 = rob2, new
        
        rob3, rob4 = 0, 0
        for y in nums2:
            new = max(rob3 + y, rob4)
            rob3, rob4 = rob4, new
        
        return max(rob2, rob4)