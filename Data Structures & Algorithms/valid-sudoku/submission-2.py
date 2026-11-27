class Solution:
    def isValidSudoku(self, board):
        def is9valid(l):
            s = set()
            for num in l:
                if num == ".":
                    continue
                if 1 <= int(num) <= 9 and num not in s:
                    s.add(num)
                else:
                    return False
            return True
        
        result = True
        for line in board:
            result &= is9valid(line)
        if result == False:
            return False
        for j in range(len(board)):
            col = [board[i][j] for i in range(len(board))]
            result &= is9valid(col)
        if result == False:
            return False
        for x in range(3):
            for y in range(3):
                block = []
                for i in range(3):
                    for j in range(3):
                        block.append(board[3*x + i][3*y + j])
                result &= is9valid(block)
        return result


                    