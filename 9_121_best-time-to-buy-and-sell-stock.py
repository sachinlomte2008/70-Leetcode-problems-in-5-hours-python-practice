class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        miner = 100000
        maxer = -1

        minerl = [0 for i in prices]
        maxerl = [0 for i in prices]

        n = len(prices)
        for i in range(n):
            if prices[i] < miner:
                miner = prices[i]
            minerl[i] = miner

            if prices[n-i-1] > maxer:
                maxer = prices[n-i-1]
            maxerl[n-i-1] = maxer

        ans = 0
        for i in range(n):
            if ans < (maxerl[i] - minerl[i]):
                ans = (maxerl[i] - minerl[i])
        
        return ans
    
'''
# Reference better solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = float('inf')
        profit = -float('inf')

        for price in prices:
            m = min(price,m)
            profit = max(price-m,profit)
        
        return profit
'''
