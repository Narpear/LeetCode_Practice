class Solution:
    def climbStairs(self, n: int) -> int:
        
        # tabulation -> on paper, this turned out to be a fibonacci sequence

        a, b = 1, 1
        for i in range(n-1):
            copy = a
            a = a + b
            b = copy
        return a