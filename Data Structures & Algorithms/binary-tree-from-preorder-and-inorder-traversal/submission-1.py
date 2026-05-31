# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # preorder : root, left, right
        # inorder: left, root, right
        # postorder: left, right, root
        if not preorder: return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        mid = inorder.index(root_val)

        # left sub tree
        left_pre = preorder[1:mid+1]
        left_in = inorder[:mid]

        root.left = self.buildTree(left_pre,left_in)

        #right subtree
        right_pre = preorder[mid+1:]
        right_in = inorder[mid+1:]

        root.right = self.buildTree(right_pre, right_in)
        return root

        