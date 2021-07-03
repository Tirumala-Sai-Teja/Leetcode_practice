class Solution:
   
    def fun(self,root,d):
        if not root:
            return 0
        l=self.fun(root.left,d)
        r=self.fun(root.right,d)
        d[0]=max(d[0],l+r)
        return max(l,r)+1
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        d=[-1]
        if not root:
            return 0
        self.fun(root,d)
        return d[0]
