# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self,root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.dfs(root.left),self.dfs(root.right),1+ max(self.dfs(root.left), self.dfs(root.left)))    

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, left + right)
            
            return 1 + max(left, right)

        dfs(root)
        return self.res