class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ls=[]
        for i,k in enumerate(nums):
            if k==target:
                ls.append(i)
        if len(ls)>0:
            r=[0]*2
            r[0],r[1]=ls[0],ls[-1]
        else:
            r=[-1,-1]
        return r


class Solution:
    def searchRange(self, arr, target):
        
        def firstOcc(arr):        
            start = 0
            end = len(arr)-1
            firstPos = -1

            while start<=end:
                mid = start + (end-start)//2

                if target == arr[mid]:
                    firstPos = mid
                    end = mid - 1

                elif target<arr[mid]:
                    end = mid-1

                else:
                    start = mid+1

            return firstPos
                    
        def lastOcc(arr):        
            start = 0
            end = len(arr)-1
            lastPos = -1

            while start<=end:
                mid = start + (end-start)//2

                if target == arr[mid]:
                    lastPos = mid
                    start = mid + 1

                elif target<arr[mid]:
                    end = mid-1

                else:
                    start = mid+1
            return lastPos
                    
        first = firstOcc(arr)
        last = lastOcc(arr)
        
        return first,last
                    
            
