class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] == x:
                return x
            else:
                return find( parent[x] )
        
        def union(x, y):
            nonlocal count
            rx = find(x)
            ry = find(y)
            if rx == ry:
                return False
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            count += 1

        count = 0
        for a,b in edges:
            union(a, b)
        return n - count
        

