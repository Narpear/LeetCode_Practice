class Solution:
    def sumOfSquares(self, n: int) -> int:
        sum = 0
        while (n>0):
            digit = n%10
            sum += digit**2
            n = n//10
        return sum

    
    def isHappy(self, n: int) -> bool:
        
        # if some sum of squares repeats during the process, it means it loops forever
        # in this case, the number is not happy

        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True

        return False