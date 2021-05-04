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
        
