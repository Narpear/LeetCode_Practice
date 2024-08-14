from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        position_speed = [[p,s] for p,s in zip(position, speed)]
        
        stack = list()

        for p, s in sorted(position_speed)[::-1]:
            time = (target-p)/s
            stack.append(time)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        
        return len(stack)