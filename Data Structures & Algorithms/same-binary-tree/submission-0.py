# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def preorder(self,p:Optional[TreeNode],l:list)->list:
        if not p:
            l.append(-1)
            return l
        l.append(p.val)

        self.preorder(p.left,l)
        self.preorder(p.right,l)
        return l

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        plist=[]
        self.preorder(p,plist)
        qlist=[]
        self.preorder(q,qlist)
        if(len(plist)!= len(qlist)):
            return False
        for i in range(len(plist)):
            if plist[i]!=qlist[i]:
                return False
        return True
        