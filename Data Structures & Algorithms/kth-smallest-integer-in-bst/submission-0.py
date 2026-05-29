# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.step = 0
        self.ans = None

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.step += 1
            if self.step == k:
                self.ans = node.val
            dfs(node.right)
        
        dfs(root)
        return self.ans