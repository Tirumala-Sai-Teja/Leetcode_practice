class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        r=0
        l=[2,3,5,7,11,13,17,19,23,29,31]
        for i in range(L,R+1):
            n=bin(i)
            c=n.count('1')
            if c in l:
                r+=1
        return r
