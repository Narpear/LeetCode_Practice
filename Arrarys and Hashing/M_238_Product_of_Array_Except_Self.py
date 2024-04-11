class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_till = [1]
        n = len(nums)

        for i in range(n-1):
            product_till.append(nums[i]*product_till[i])

        # print(product_till)

        product_beyond = [1]*n

        for i in range(n-2, -1, -1):
            product_beyond[i] = product_beyond[i+1]*nums[i+1]

        # print(product_beyond)

        for i in range(n):
            product_beyond[i] = product_beyond[i]*product_till[i]

        return product_beyond