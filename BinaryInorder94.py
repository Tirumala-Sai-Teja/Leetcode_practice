class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[root.val]
        return self.inorderTraversal(root.left)+res+self.inorderTraversal(root.right)
    
    
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.inorder(ans,root)
        return ans
    def inorder(self,ans,root):
        if not root:
            return 
        self.inorder(ans,root.left)
        ans.append(root.val)
        self.inorder(ans,root.right)
           
