# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def getDepth(node):
            if not node:
                return 0
            leftDepth= getDepth(node.left)
            rightDepth = getDepth(node.right)
            self.res = max(self.res, (leftDepth+rightDepth))
            return max(leftDepth, rightDepth) + 1
        
        getDepth(root)
        return self.res