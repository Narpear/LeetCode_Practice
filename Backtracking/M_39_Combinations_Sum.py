from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        current = []

        def dfs(i, current, total):
            if total == target:
                result.append(current.copy())
                return
            if i >= len(candidates) or total>target:
                return

            # to include candidates[i]
            current.append(candidates[i])
            dfs(i, current, total+candidates[i])

            # to not include candidates[i]
            current.pop()
            dfs(i+1, current, total)

        dfs(0, [], 0)
        return result