class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height);
        l, r = 0, n-1
        left_max, right_max = height[l], height[r]
        sum = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                sum += (left_max - height[l])
            else:
                r -= 1
                right_max = max(right_max, height[r])
                sum += (right_max - height[r])
        return sum

            

        