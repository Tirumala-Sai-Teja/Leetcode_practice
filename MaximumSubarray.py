class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=len(nums)
        c=maxsum=nums[0]
        for i in range(1,l):
            c=max(nums[i],c+nums[i])
            if maxsum<c:
                maxsum=c
        return maxsum
      
 '''''method 2:
 class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=len(nums)
        maxsum=nums[0]
        for i in range(l):
          for j in range(i+1,l+1):
            s=sum(nums[i:j])
            if s>maxsum:
              maxsum=s
       return maxsum''''''
            
