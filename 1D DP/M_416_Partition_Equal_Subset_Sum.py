from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)        
        if total%2==1:
            return False
        
        target = total//2
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            new_dp = set()
            for element in dp:
                curr_sum = nums[i] + element
                if curr_sum == target:
                    return True
                new_dp.add(curr_sum)
                new_dp.add(element)
            dp = new_dp
        return False      

