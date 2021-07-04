class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> ans;
        queue<TreeNode*> q;
        if(root == NULL){
            return ans;
        }
        q.push(root);
        while(q.empty()==false)
        {
            int c;
            c=q.size();
            vector<int> v;
            while(c--){
                v.push_back(q.front()->val);
                if(q.front()->left!=NULL)
                    q.push(q.front()->left);
                if(q.front()->right!=NULL)
                    q.push(q.front()->right);
                q.pop();
            }
            ans.push_back(v);
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
