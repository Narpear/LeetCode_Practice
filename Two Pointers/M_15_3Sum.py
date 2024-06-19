from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)

        for i, number in enumerate(nums):
            # making sure we do not generate duplicate triplets
            if i>0 and number==nums[i-1]:
                continue
            
            # actual three sum logic: at each element, perform 2SumII of the rest of the array
            left = i+1
            right = n-1
            while (left<right):
                sum = number + nums[left] + nums[right]
                if sum>0:
                    right-=1
                elif sum<0:
                    left+=1
                else:
                    result.append([number, nums[left], nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
        return result