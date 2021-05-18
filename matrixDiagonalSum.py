class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        k=len(mat)
        s=0
        for i in range(k):
            for j in range(k):
                if i==j:
                    s+=mat[i][j]
                elif i+j==k-1:
                    s+=mat[i][j]
        return s
       
                    
        
