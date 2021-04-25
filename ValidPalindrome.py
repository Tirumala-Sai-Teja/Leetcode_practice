''''class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=''
        s=s.lower()
        k='qwertyuiopasdfghjklzxcvbnm1234567890'
        for i in s:
            if i in k:
                result+=i
        return result==result[::-1]'''''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        list=[]
        s=s.lower()
        for i in range (0,len(s)):
            if 123>ord(s[i])>96 or 58>ord(s[i])>47:
              list.append(s[i])
        return list==list[::-1]
            
class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=''
        for i in s:
            if i.isalnum():
                result+=i
        result=result.lower()
        print(result)
        if result[::]==result[::-1]:
            return 1
        else:
            return 0
        
            
        
