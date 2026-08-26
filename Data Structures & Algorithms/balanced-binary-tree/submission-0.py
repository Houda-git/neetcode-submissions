# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if abs(self.diameter(root.right) - self.diameter(root.left)) >= 2:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def diameter(self, root):
        if root is None:
            return 0
        return 1 + max(self.diameter(root.right), self.diameter(root.left))