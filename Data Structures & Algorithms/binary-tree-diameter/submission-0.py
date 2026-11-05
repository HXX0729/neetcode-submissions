# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
       
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            nonlocal res
            if root is None:
                return 0
            left_depth = depth(root.left)
            right_depth = depth(root.right)
            diameter = left_depth + right_depth
            if diameter > res:
                res = diameter
            return max(left_depth, right_depth) + 1

        res = 0
        depth(root)
        return res
