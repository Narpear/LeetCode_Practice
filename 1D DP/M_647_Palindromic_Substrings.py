class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            # check for odd length palindromes centred at s[i]
            l, r = i, i
            while l>=0 and r<len(s) and s[l]==s[r]:
                count += 1
                l -= 1
                r += 1
            
            # check for even length substrings centred at s[i] and s[i+1]
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                count += 1
                l -= 1
                r += 1
            
        return count