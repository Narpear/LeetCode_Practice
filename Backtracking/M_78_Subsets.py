
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        subset = []
        def dfs(i):
            if i>=len(nums):
                result.append(subset.copy())
                return
            
            # include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # not include nums[i]
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return result