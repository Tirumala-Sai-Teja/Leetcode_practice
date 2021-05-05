class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split(' ')
        l=l[-1::-1]
        s=''
        for i in l:
            if len(i)>0:
                s+=i+' '
        return s.strip()
    
