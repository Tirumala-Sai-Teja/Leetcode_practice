class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx=-9999999
        result=0
        for i in range(len(prices)-1,-1,-1):
            if prices[i]>maxx:
                maxx=prices[i]
            elif (maxx-prices[i])>result:
                result=maxx-prices[i]
        return result
   #using dynamic programming top down
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l=prices
        k=[0]*len(l)
        m=[0]*len(l)
        
        m[-1]=k[-1]-l[-1]


        for i in range(len(l)-2,-1,-1):
            k[i]=max(l[i+1],k[i+1])
            m[i]=k[i]-l[i]
            
    
        return(max(m) if max(m)>0 else 0)
