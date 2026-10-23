class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            n = len(s)
            block = str(n) + "\\" + s
            encoded += block
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)
        res = []
        while i < n:
            j = i
            while s[j] != '\\':
                j += 1
            length = int(s[i: j])
            res.append(s[j+1: j + 1+ length])
            i = j + 1 + length
        return res

