class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join([character for character in s if character.isalnum()]).lower()
        n = len(s)
        # print(s)

        i = 0
        j = n-1

        while j>i:
            # print(s[i], s[j])
            if s[i]==s[j]:
                i += 1
                j -= 1
                continue
            else:
                return False

        return True