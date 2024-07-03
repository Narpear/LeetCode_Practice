from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # any number XORed with itself gives zero. 
        # XOR all elements of the list
        # the final result should be the only number without a duplicate

        result = nums[0]
        n = len(nums)
        for i in range(1, n):
            result = result^(nums[i])
        return result