# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def level(index, root):
            if not root:
                return res
            if len(res)<index:
                res.append([])
            res[index-1].append(root.val)
            if root.left:
                level(index+1, root.left)
            if root.right:
                level(index+1, root.right)

        level(1, root)
        return res
