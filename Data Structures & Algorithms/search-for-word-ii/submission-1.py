class Node:
    def __init__(self, val=0):
        self.val = val
        self.children = {}
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        for word in words:
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = Node()
                cur = cur.children[ch]
            cur.val = word
        
        def dfs(i, j, node):

            if board[i][j] not in node.children:
                return False
            tmp = board[i][j]
            board[i][j] = "#"

            for x,y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0<= x < len(board) and 0<= y < len(board[0]):
                    dfs(x, y, node.children[tmp])

            board[i][j] = tmp

            if node.children[tmp].val != 0:
                result.append(node.children[tmp].val)
                node.children[tmp].val = 0
        
        result = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                    dfs(i,j, root)
        return result


        