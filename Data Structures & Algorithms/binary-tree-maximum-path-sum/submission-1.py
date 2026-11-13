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
            #return the max value if splits here, and not splits here, and update the result    
            nonlocal result
            if not root:
                return (0, 0)
            
            left_split, left_unsplit = maxPath(root.left)
            right_split, right_unsplit = maxPath(root.right)

            left_split = left_split if left_split > 0 else 0
            left_unsplit = left_unsplit if left_unsplit > 0 else 0
            right_split = right_split if right_split > 0 else 0
            right_unsplit = right_unsplit if right_unsplit > 0 else 0

            #if splits here
            split_sum = root.val + left_unsplit + right_unsplit

            #if unsplit here
            unsplit_sum = root.val + max(left_unsplit, right_unsplit)


            result = max(result, split_sum, unsplit_sum)
            return (split_sum, unsplit_sum)

        maxPath(root)
        return result


