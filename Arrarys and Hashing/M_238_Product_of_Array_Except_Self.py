from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product_till = [1]*n
        product_beyond = [1]*n

        for i in range(1, n):
            product_till[i] = product_till[i-1]*nums[i-1]
            
        # print(product_till)

        for i in range(n-2, -1, -1):
            product_beyond[i] = product_beyond[i+1]*nums[i+1]

        # print(product_beyond)

        for i in range(1, n):
            product_beyond[i] *= product_till[i]

        # print(product_beyond)

        return product_beyond