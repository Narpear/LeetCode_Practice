class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = ''.join([character for character in s if character.isalnum()]).lower()
        # print(string)
        n = len(string)

        i = 0
        j = n-1

        while(i<j):
            if string[i]!=string[j]:
                return False
            i += 1
            j -= 1

        return True
        