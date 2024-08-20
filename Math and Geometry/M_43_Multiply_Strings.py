class Solution:
    def string_to_int(self, s: str):
        n = len(s)
        number = 0
        for i in range(n):
            digit = ord(s[i])-48
            number = number*10 + digit
        return number

    def integer_to_str(self, n: int):
        string = ""
        while n>0:
            digit = n%10
            string = chr(digit+48) + string
            # print(string)
            n = n//10
        return string
    
    def multiply(self, num1: str, num2: str) -> str:
        n1 = self.string_to_int(num1)
        n2 = self.string_to_int(num2)

        if n1 == 0  or n2 == 0:
            return "0"

        # print(n1, n2)
        prod = self.integer_to_str(n1*n2)
        return prod