class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #树的必要条件1: 边数=n-1
        if len(edges) != n-1:
            return False

        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        #树的必要条件2: 联通，采取dfs遍历，能走遍所有节点就是联通
        visited = set()
        stack = []
        stack.append(0)

        while stack:
            cur = stack.pop()
            visited.add(cur)
            for neighbor in graph[cur]:
                if neighbor not in visited:
                    stack.append(neighbor)
        return len(visited) == n
        
