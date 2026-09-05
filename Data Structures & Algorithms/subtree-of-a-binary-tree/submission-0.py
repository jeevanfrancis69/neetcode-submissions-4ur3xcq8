# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True

        if root is None:
            return False

        if (self.isSame(root,subRoot)):
            return True

        return (self.isSubtree(root.right, subRoot) or                self.isSubtree(root.left, subRoot))
        
        
    def isSame(self, root:Optional[TreeNode], root1:Optional[TreeNode]):
            if not root and not root1:
                return True
            
            if not root or not root1:
                return False
            
            if (root.val != root1.val):
                return False
            else:
                return (self.isSame(root.right , root1.right) and self.isSame(root.left, root1.left))



        