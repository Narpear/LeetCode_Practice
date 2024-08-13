from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(i, total, current):
            if total==target:
                result.append(current.copy())
                return
            if (i>=len(candidates) or total>target):
                return 
            
            # to include candidates[i]
            current.append(candidates[i])
            dfs(i+1, total+candidates[i], current)

            # to not include candidates[i]
            current.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i += 1
            dfs(i+1, total, current)    

        dfs(0, 0, [])
        return result