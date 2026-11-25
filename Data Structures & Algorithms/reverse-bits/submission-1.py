class Solution:
    def reverseBits(self, n: int) -> int:
        binaries = []
        for i in range(32):
            binaries.append(n & 1)
            n >>= 1
        res = 0
        for b in binaries:
            res = res << 1 | b
        return res