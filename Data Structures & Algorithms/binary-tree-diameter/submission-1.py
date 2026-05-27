# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # go all the way down to one branch, travel back
        # while traveling back, count what's the max edges

        self.res = 0
        def getDepth(node):
            #base case
            if not node:
                return 0
            leftH = getDepth(node.left)
            rightH = getDepth(node.right)

            self.res = max(self.res, leftH + rightH)
            return max(leftH, rightH) + 1

        getDepth(root)
        return self.res
        