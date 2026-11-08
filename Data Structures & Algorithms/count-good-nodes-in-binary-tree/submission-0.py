# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, greatest):
            if not node:
                return
            nonlocal count
            if node.val >= greatest:
                count += 1
                greatest = node.val
            dfs(node.left, greatest)
            dfs(node.right, greatest)
        
        count = 0
        dfs(root, root.val)
        return count

