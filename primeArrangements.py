from math import *
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        c=0
        for i in range(2,n+1):
            for j in range(2,i//2+1):
                if i%j==0:
                    break
            else:
                c+=1
        return (factorial(c)*factorial(n-c))%1000000007
                
        
