from math import *
class Solution:
    def trailingZeroes(self, n: int) -> int:
        c=0
        p=1
        
        while(n>0):
            n=n//5
            c+=n
        
        return c
