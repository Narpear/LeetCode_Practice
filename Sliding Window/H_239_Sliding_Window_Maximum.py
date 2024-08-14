from typing import List
import collections

# # my TLE solution T_T

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         window = nums[:k]
#         result = []

#         lp = 0
#         for rp in range(k, len(nums)+1):
#             window = nums[lp:rp]
#             x = max(window)    
#             result.append(x)
#             lp += 1

#         return result


# The actual solution

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l, r = 0, 0 

        q = collections.deque()      # indices

        while (r<len(nums)):
            # pop smaller values from q and append when this is smaller
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            
            # pop left value from window if out of bounds
            if l>q[0]:
                q.popleft()
            
            if (r+1)>=k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output




