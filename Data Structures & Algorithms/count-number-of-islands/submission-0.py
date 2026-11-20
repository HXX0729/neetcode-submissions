class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        def sinkIsland(x, y):
            if grid[x][y] == "1":
                grid[x][y] = "0"
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    newx, newy = x + dx, y + dy
                    if 0 <= newx < row and 0 <= newy < col:
                        sinkIsland(newx, newy)

        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    count += 1
                    sinkIsland(i, j)
        return count