# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    
    def sameTree(self, root, sub_root):
        if not root and not sub_root:
            return True
        if root and sub_root and root.val == sub_root.val:
            return self.sameTree(root.left, sub_root.left) and self.sameTree(root.right, sub_root.right)
        else:
            return False