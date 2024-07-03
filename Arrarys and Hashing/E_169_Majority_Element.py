from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        n = len(nums)
        threshold = n//2

        for number in nums:
            if number in counts:
                counts[number] += 1
            else:
                counts[number] = 1
            if counts[number] > threshold:
                return number
        return