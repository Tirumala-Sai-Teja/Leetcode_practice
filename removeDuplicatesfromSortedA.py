class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is []:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            ori = len(nums)
            nums.extend(list(dict.fromkeys(nums)))
            del nums[0:ori]
            return len(nums)
