class Solution:
    def scoreOfString(self, s: str) -> int:
        i = len(s)
        if i==0:
            return 0
        sum = 0
        for n in range(i-1):
            sum = sum+abs(ord(s[n])-ord(s[n+1]))
        return sum  