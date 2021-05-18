class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        c=1
        s=a
        while len(a)<len(b):
            a+=s
            c+=1
        if b in a:
            return c
        else:
            a+=s
            print(a)
            if b in a:
                return c+1
            return -1
            
