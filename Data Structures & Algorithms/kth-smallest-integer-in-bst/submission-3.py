# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder(root,  k):
            nonlocal count

            if root is None:
                return None

            left = inorder(root.left,  k)
            if left is not None:
                return left

            count += 1
            if count == k:
                return root.val

            right = inorder(root.right,  k)
            if right is not None:
                return right
            
            return None
        
        count = 0
        return inorder(root, k)
            
        
