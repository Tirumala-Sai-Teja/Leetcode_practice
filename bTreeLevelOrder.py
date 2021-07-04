from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans=[]
        if not root:
            return ans
        r=deque([root])
        while r:
            v=[]
            for i in range(len(r)):
                n=r.popleft()
                v.append(n.val)
                if n.left:
                    r.append(n.left)
                if n.right:
                    r.append(n.right)
            ans.append(v)
        return ans[::-1]
