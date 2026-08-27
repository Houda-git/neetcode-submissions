# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # the subRoot is never None
        def sameTree(root, subRoot):
            if subRoot is None and root is None:
                return True
            if root is None or subRoot is None: 
                return False
            return (root.val == subRoot.val and sameTree(root.right, subRoot.right) and sameTree(root.left, subRoot.left)) 
        if root is None:
            return False
        if sameTree(root, subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
    