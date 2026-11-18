class Node:
    def __init__(self, val = -1):
        self.val = 0
        self.children = {}
        self.end = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node(ch)
            cur = cur.children[ch]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        if cur.end == False:
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return True
        
        