# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        def preorder(root):
            nonlocal res
            if not root:
                res += "None,"
                return
            res += str(root.val) + ","
            preorder(root.left)
            preorder(root.right)
            return
        preorder(root)
        
        print(res)
        return res
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def reconstruct():
            nonlocal p
            nonlocal seq
            if p == len(seq):
                return
            if seq[p] == "None":
                p += 1
                return None
            if seq[p] != "None" or seq[p] != "":
                val = int(seq[p])
                p += 1
                cur = TreeNode(val)
                cur.left = reconstruct()
                cur.right = reconstruct()
                return cur
            return

        if data == "":
            return None
        p = 0
        seq = data.split(',')
        return reconstruct()
        
        
       
                






