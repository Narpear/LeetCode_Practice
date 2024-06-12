from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_height_left = [0]*n
        max_height_right = [0]*n

        for i in range(1, n):
            max_height_left[i] = max(height[i-1], max_height_left[i-1])
        
        for i in range(n-2, -1, -1):
            max_height_right[i] = max(height[i+1], max_height_right[i+1])
    
        sum = 0
        for i in range(n):
            sum += max(0, (min(max_height_left[i], max_height_right[i]) - height[i]))

        return sum