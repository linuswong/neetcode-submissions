class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minB = prices[0]

        for cur in prices:
            maxP = max(cur-minB, maxP)
            minB = min(minB, cur)

        return maxP


        
        # l,r = 0,len(prices) - 1
        # maxP = 0
        # while l!=r:
        #     calc = prices[r] - prices[l]
        #     maxP = max(calc,maxP)

        #     if prices[l]-prices[l+1] >= prices[r-1] - prices[r] :
        #         l+=1
        #     else:
        #         r-=1
        # return max