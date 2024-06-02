class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # val:index

        for index, number in enumerate(nums):
            # print(index, number)
            if (target-number) in hashmap:
                return(index, hashmap[target-number])
            hashmap[number] = index