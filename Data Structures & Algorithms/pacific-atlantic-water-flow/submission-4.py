class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(x, y, visited):
            if (x, y) in visited:
                return
            visited.add((x,y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < row and 0 <= new_y < col:
                    if heights[new_x][new_y] >= heights[x][y]:
                        dfs(new_x, new_y, visited)
        row = len(heights)
        col = len(heights[0])
        pacific, atlantic = set(), set()

        for y in range(col):
            dfs(0, y, pacific)
            dfs(row-1, y, atlantic)
        for x in range(row):
            dfs(x, 0, pacific)
            dfs(x, col-1, atlantic)
        return list(pacific & atlantic)

            
            