# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validateRoot(low, root, high):
            if not root:
                return True

            if (not (low < root.val < high)):
                return False
            else:
                return (validateRoot(low, root.left, root.val) and validateRoot(root.val, root.right,high))
        

        return validateRoot(float('-inf'), root, float('inf'))