class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, d = 0, len(matrix) - 1
        while u <= d:
            mid = (u + d)//2
            print(u, d, mid)
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                d = mid - 1
            else:
                u = mid + 1
        
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[d][mid] > target:
                r = mid - 1
            elif matrix[d][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False