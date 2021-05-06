class Solution:
    def countBits(self, num: int) -> List[int]:
        l=[]
        for i in range(num+1):
            n=bin(i)
            s=str(n)
            l.append(s.count('1'))
        return l
