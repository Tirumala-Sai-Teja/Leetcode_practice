class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        a=nums[:]
        b=nums[:]
        for i in range(len(nums)-1):
            if a[i]>a[i+1]:
                del a[i]
                break
        for i in range(len(nums)-1):
            if b[i]>b[i+1]:
                del b[i+1]
                break
        c=sorted(a)
        d=sorted(b)
        if c==a or d==b:
            return 1
        return 0
        
        
