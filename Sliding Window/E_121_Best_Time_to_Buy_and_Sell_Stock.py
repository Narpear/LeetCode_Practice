class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_future = [0]*n
        max_future[n-1] = 0
        for i in range(n-2, -1, -1):
            max_future[i] = max(max_future[i+1],prices[i+1])
        
        for i in range(n):
            max_future[i] = max_future[i] - prices[i]

        max_profit = max(max_future)
        return (max(max_profit, 0))