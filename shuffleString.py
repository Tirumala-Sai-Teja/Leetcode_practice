class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d=dict(zip(indices,s))
        l=[0]*len(s)
        for i in d.keys():
            l[i]=d[i]
        return ''.join(l)
