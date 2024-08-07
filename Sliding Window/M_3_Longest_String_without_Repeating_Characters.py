class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        result = 0
        n = len(s)
        
        for r in range(n):
            while(s[r] in charset):
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            result = max(result, (r-l+1))
        return result