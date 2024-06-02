class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return (sorted(s) == sorted(t))


# #alternate solution
#     def isAnagram(self, s: str, t: str) -> bool:
#         s_count = {}
#         t_count = {}

#         for character in s:
#             if character in s_count:
#                 s_count[character] += 1
#                 continue
#             s_count[character] = 1

#         for character in t:
#             if character in t_count:
#                 t_count[character] += 1
#                 continue
#             t_count[character] = 1

#         if s_count==t_count:
#             return True
#         return False