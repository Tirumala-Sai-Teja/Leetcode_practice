class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        f=0
        d={')':'(',']':'[','}':'{'}
        if len(l)%2!=0:
            return 0
        for i in s:
            le=len(l)
            if i in d.keys():
                #print(l.pop(),d[i])
                if le==0 or d[i] !=l.pop() :
                    return False
            else:
                l.append(i)
        if  len(l)!=0:
            return 0
        return 1
