from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        nums.sort()

        def dfs(i):
            if i>=len(nums):
                result.append(curr.copy())
                return
            
            # to include nums[i]
            curr.append(nums[i])
            # print("First: ", curr, result)
            dfs(i+1)
            # print("After adding element: ", curr, result)

            # to not include nums[i], and also skip through repeats
            curr.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i += 1
            dfs(i+1)
            # print("After popping element: ", curr, result)
        
        dfs(0)
        return result