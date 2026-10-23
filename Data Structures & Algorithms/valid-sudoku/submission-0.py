class Solution:
    def isRowValid(self, row):
        l = []
        for num in row:
            if num != '.':
                l.append(num)
        return len(set(l)) == len(l)
           
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for row in board:
            if not self.isRowValid(row):
                return False
        
        for j in range(n):
            col = []
            for i in range(n):
                col.append(board[i][j])
            if not self.isRowValid(col):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = []
         
                block = board[i][j: j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                if not self.isRowValid(block):
                    return False

        
        return True