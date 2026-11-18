class Node:
    def __init__(self):
        self.val = 0
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                new = Node()
                new.val = ch
                cur.children[ch] = new
            cur = cur.children[ch]
        cur.end = True


    def search(self, word: str) -> bool:

        def backtracking(root, start):
            if start == len(word):
                if root.end == True:
                    return True
                else:
                    return False
            ch = word[start]
            success = False
            if ch == '.':
                for k, v in root.children.items():
                    success = success or backtracking(v, start + 1)
            else:
                if ch not in root.children:
                    return False
                success = success or backtracking(root.children[ch], start + 1)
            return success

        return backtracking(self.root, 0)

        
        
