class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for number in nums:
            if number not in nums_set:
                nums_set.add(number)
                continue
            return True
        return False