"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        def dfs(node):
            if node is None:
                return None
                
            cur = Node(node.val)
            visited[node] = cur

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    cur.neighbors.append(dfs(neighbor))
                else:
                    cur.neighbors.append(visited[neighbor])
            return cur

        visited = {}
        return dfs(node)