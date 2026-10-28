class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            #left is in order
            if nums[mid] >= nums[0]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            #right is in order
            else:
                if nums[mid] <= target <= nums[r]:
                    l = l + 1
                else:
                    r = mid - 1
        return -1

