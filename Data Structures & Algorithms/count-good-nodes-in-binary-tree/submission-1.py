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
                return 0
            count = 0
            if node.val >= greatest:
                count += 1
                greatest = node.val
            count += dfs(node.left, greatest)
            count += dfs(node.right, greatest)
            return count
        

        return dfs(root, root.val)

