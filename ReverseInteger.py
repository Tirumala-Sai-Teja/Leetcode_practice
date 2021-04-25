class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        s=s[::-1]
        if x<0:
             s=s[-1]+s[:-1]
        x=int(s)
        if x>-(2**31) and x<(2**31)-1:
            return x
        else:
            return 0
        
          
        
        
            
