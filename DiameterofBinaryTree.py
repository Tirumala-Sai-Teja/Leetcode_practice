class Solution {
public:
    int d;
    int fun(TreeNode *root){
        if(root==NULL)
            return 0;
        int l= fun(root->left);
        int r=fun(root->right);
        d=max(d,l+r);
        return max(l,r)+1;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        if(root==NULL)
            return 0;
        fun(root);
        return d;
        
    }
};
