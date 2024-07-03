from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashmap solution
        # counts = {}
        # n = len(nums)
        # threshold = n//2

        # for number in nums:
        #     if number in counts:
        #         counts[number] += 1
        #     else:
        #         counts[number] = 1
        #     if counts[number] > threshold:
        #         return number
        # return

        # moore's majority voting algorithm
        count = 0
        element = 0
        for number in nums:
            if count==0:
                element = number
            if number==element:
                count += 1
            else:
                count -= 1
            
        return element