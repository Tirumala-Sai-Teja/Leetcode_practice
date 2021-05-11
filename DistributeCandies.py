class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s=set(candyType)
        l1=len(candyType)//2
        l2=len(s)
        print(l1,l2)
        if l2<=l1:
            return l2
        if l2>l1:
            return l1
        
