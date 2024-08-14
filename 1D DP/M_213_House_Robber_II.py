from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            a, b = 0, 0
            for n in nums:
                temp = max(a+n, b)
                a = b
                b = temp
            return b
        
        if len(nums)==0: return 0
        if len(nums)==1: return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))