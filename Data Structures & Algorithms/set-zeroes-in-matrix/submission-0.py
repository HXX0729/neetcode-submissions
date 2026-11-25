class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = set()
        col = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j] = 0
        