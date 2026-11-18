class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 

        def isValid(i, j):
            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                return True
            else:
                return False

        def backtracking(i, j, k):
            if k == len(word):
                return True
            if not isValid(i, j):
                return False
            if board[i][j] != word[k]:
                return False

            found = False

            tmp = board[i][j]
            board[i][j] = '#'
            for d in directions:
                x = i + d[0]
                y = j + d[1]
                found = found or backtracking( x, y, k + 1)
            board[i][j] = tmp
            
            return found
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(backtracking( i, j, 0)):
                    return True
        return False


