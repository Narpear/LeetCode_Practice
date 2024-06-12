from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        lp = 0
        rp = n-1
        max_water = 0

        while lp<rp:
            water = min(height[lp], height[rp])*(rp-lp)
            max_water = max(max_water, water)
            if height[lp]>height[rp]:
                rp -= 1
            else:
                lp += 1

        return max_water
