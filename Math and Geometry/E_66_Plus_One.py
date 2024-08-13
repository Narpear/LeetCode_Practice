class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        power = 0
        n = len(digits)
        for i in range(n-1,-1,-1):
            digit = digits[i]
            number = number + digit*(10**power)
            power += 1

        # print(number)
        number += 1
        digits = []

        while number>0:
            digit = number%10
            number = number//10
            digits.insert(0, digit)
        
        return digits