from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
       # tabulation
        cost.append(0)
        for i in range(len(cost)-3, -1, -1):
            print(cost[i])
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1]) 

        # # memoization
        # def dp(i):
        #     # base case:
        #     if i<2:
        #         return cost[i]
        #     return cost[i] + min(dp(i-1), dp(i-2))
        
        # return min(dp(len(cost)-1), dp(len(cost)-2))

