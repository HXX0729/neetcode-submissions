class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        target = nums[r]
        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid)
            if nums[mid] > target:
                l = mid + 1
            elif nums[mid] == target:
                return nums[mid]
            else:
                r = mid - 1
        return nums[l]
