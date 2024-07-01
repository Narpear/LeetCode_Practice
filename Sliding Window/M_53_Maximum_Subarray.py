from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # sliding window solution
        # left pointer is incremented if the prefix sum becomes negative
        # right pointer is always incremented

        maxSub = nums[0]
        current_sum = 0

        for number in nums:
            if current_sum<0:
                current_sum = 0
            current_sum += number
            maxSub = max(maxSub, current_sum)