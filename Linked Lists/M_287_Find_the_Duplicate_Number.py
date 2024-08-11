# #  the easy way with hash maps and O(n) extra space

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         count_map = {}
#         for number in nums:
#             count_map[number] = count_map.get(number, 0) + 1
#             if count_map[number]!=1:
#                 return number
#         return -1

