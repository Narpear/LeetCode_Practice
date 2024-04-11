class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0

        left_ptr = 0
        right_ptr = n-1

        while(left_ptr<right_ptr):
            area = (right_ptr-left_ptr)*min(height[left_ptr], height[right_ptr])
            if height[left_ptr]>height[right_ptr]:
                right_ptr -= 1
            else:
                left_ptr += 1
            max_area = max(max_area, area)

        return max_area
