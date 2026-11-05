# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_height(root):
            if root is None:
                return True, 0

            left_balanced, left_height = get_height(root.left)
            right_balanced, right_height = get_height(root.right)

            if abs(left_height - right_height) > 1 or not left_balanced or not right_balanced:
                balanced = False
            else:
                balanced = True
            return balanced, max(left_height, right_height) + 1

        return get_height(root)[0]




