class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for number in nums:
            if number in hashset:
                return True
            hashset.add(number)
        return False
    
## alternate solution 
# nums_set = set(nums)
# n = len(nums)
# m = len(nums_set)
# if n==m:
# return False
# return True