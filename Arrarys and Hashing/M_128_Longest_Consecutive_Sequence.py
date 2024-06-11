class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_sequence_length = 0

        for n in nums:
            #check if the number is the start of a sequence
            if (n-1) not in nums_set:
                length = 0
                while(n+length) in nums_set:
                    length += 1
                longest_sequence_length = max(longest_sequence_length, length)

        return longest_sequence_length
