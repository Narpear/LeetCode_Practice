from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        permutations = self.permute(nums[1:])
        result = []
        for element in permutations:
            for i in range(len(element)+1):
                element_copy = element.copy()
                element_copy.insert(i, nums[0])
                result.append(element_copy)
        return result