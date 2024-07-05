from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        current_sum = 0
        prefix_sums = {0:1}

        for number in nums:
            current_sum += number
            difference = (current_sum - k)
            
            # if difference in prefix_sums:
            #     result += prefix_sums[difference]
            # if current_sum in prefix_sums:
            #     prefix_sums[current_sum] += 1
            # else:
            #     prefix_sums[current_sum] = 1

            result += prefix_sums.get(difference, 0)
            prefix_sums[current_sum] = 1 + prefix_sums.get(current_sum, 0)
        
        return result