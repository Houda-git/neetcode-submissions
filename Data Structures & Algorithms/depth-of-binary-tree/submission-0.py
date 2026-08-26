# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxdep(root, val):
            if not root:
                return val
            if root.right and not root.left:
                return maxdep(root.right, val+1)
            elif root.left and not root.right:
                return maxdep(root.left, val+1)
            else:
                return max(maxdep(root.left, val+1), maxdep(root.right, val+1))
        return maxdep(root, 0)
            