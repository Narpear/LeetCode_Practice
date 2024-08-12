from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = int((n*(n+1))/2)
        for element in nums:
            sum = sum - element
        return sum