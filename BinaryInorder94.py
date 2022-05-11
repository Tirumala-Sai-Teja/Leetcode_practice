class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[root.val]
        return self.inorderTraversal(root.left)+res+self.inorderTraversal(root.right)
    
