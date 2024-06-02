class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for number in nums:
            if number not in nums_set:
                nums_set.add(number)
                continue
            return True
        return False
    
## alternate solution 
# nums_set = set(nums)
# n = len(nums)
# m = len(nums_set)
# if n==m:
# return False
# return True