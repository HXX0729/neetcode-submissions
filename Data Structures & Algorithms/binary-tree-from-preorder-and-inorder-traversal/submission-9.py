# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre = 0
        idx = {v: i for i, v in enumerate(inorder)}
        def build(l, r):
            if l > r:
                return None
            nonlocal pre
            root = TreeNode(preorder[pre])
            pre += 1
            mid = idx[root.val]
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root
        return build(0, len(preorder) - 1)

