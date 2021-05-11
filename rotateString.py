class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A==B:
            return True
        else:
            for i in range(len(A)-1):
                x=''
                x+=A[i+1:]
                x+=A[0:i+1]
                if x==B:
                    return 1
            else:
                return 0
       
       
