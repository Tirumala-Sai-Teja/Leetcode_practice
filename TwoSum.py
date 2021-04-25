class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            ind=nums.index(i)
            if (target-i) in nums[ind+1:] :
                if ind!=nums.index(target-i,ind+1):
                
                     return [nums.index(i),nums.index(target-i,ind+1)]
        
