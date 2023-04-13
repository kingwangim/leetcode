# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def preorder(root: TreeNode):
            if not root: return res
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        res = []
        preorder(root)
        for i in range(len(res)):
            if k-res[i] in res[i+1:]:
                return True
        return False