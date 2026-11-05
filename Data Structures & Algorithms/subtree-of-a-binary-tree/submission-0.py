# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            left_id = isIdentical(p.left, q.left)
            right_id = isIdentical(p.right, q.right)
            return p.val == q.val and left_id and right_id
        
        if root is None:
            return False
        return isIdentical(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

