# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # DFS, find the sum of the sub trees, and compare with the cur max
        self.res = float('-inf')

        def dfs(node):
            if not node: 
                return 0 
            
            left = dfs(node.left)
            left = max(left, 0)
            right = dfs(node.right)
            right = max(right, 0)
            self.res = max(self.res, left + node.val + right)
            
            return max(left,right) + node.val
        
        dfs(root)
        return self.res

        
            