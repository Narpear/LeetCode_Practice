class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for character in t:
            countT[character] = countT.get(character, 0) + 1
        
        have = 0
        need = len(t)

        result, result_length = [-1, -1], float("inf")

        l = 0
        for r in range(len(s)):
            character = s[r]
            window[character] = window.get(character, 0) + 1

            if character in countT and (countT[character] == window[character]):
                have += 1
            
            while have==need:
                if (r-l+1)<result_length:
                    result = [l,r]
                    result_length = (r-l+1)
                window[s[l]] -= 1
                if s[l] in countT and (window[s[l]]<countT[s[l]]):
                    have -= 1
                l += 1

        l, r = result
        return s[l: r+1] if result_length!=float('inf') else ""
