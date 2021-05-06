class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a=['a','e','i','o','u']
        l=len(s)
        s=s.lower()
        s1=s[:l//2]
        s2=s[l//2:]
        c1,c2=0,0
        for i in s1:
            if i in a:
                c1+=1
        for i in s2:
            if i in a:
                c2+=1
        print(c1,c2)
        if c1==c2:
            return 1
        return 0
