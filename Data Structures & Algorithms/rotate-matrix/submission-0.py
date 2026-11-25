class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for line in matrix:
            for j in range(n//2):
                line[j], line[n-1-j] = line[n-1-j], line[j]
        

