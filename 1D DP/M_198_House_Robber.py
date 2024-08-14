from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # tabulation
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        nums[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            nums[i] = max((nums[i] + nums[i-2]), nums[i-1])
        
        return nums[n-1]


        # # memoization
        # def cost(i):
        #     if i==0:
        #         return nums[0]
        #     if i==1:
        #         return max(nums[0], nums[1])            
        #     return max((nums[i] + cost(i-2)), cost(i-1))
        
        # n = len(nums)
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return nums[0]
        
        # return max(cost(n-1), cost(n-2))

        