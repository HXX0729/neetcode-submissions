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
            nonlocal ans

            if ans is not None:
                return 

            if root is None:
                return None

            left = inorder(root.left,  k)
            

            count += 1
            if count == k:
                ans = root.val
                return

            right = inorder(root.right,  k)
                       
            return
        
        count = 0
        ans = None
        inorder(root, k)
        return ans
            
        
