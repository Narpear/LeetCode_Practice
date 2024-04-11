class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        set_nums = set(nums)
        counts = {}
        for number in set_nums:
            counts[number] = nums.count(number)

        # print("counts: ", counts)

        counts = [(key, value) for key, value in counts.items()]
        # print("counts: ", counts)

        counts.sort(key = lambda x:x[1], reverse = True)
        # print("most elements", counts)

        result = [a for (a,b) in counts][:k]
        return result