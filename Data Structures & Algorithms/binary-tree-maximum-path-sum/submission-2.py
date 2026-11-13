# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')
        def maxPath(root):
            nonlocal result
            if not root:
                return 0
            left = max(maxPath(root.left), 0)
            right = max(maxPath(root.right), 0)

            #if split here
            result = max(result, root.val + left + right)

            #return the unsplit max sum
            return root.val + max(left, right)

        maxPath(root)
        return result

