# monotonic decreasing stack
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0]*len(temperatures)
        stack = []  # pairs of (temp, index)

        for i, temp in enumerate(temperatures):
            while stack and temp>stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                answer[stackIndex] = (i-stackIndex)
            stack.append([temp, i])           

        return answer