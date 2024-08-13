class Solution:
    def reverseBits(self, n: int) -> int:
        result = ""
        for i in range(32):
            remainder = n%2
            result = str(remainder) + result
            n = n//2
        
        # print(result)
        result = result[::-1]
        return int("0b"+result, 2)