class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")":"(", "}":"{", "]":"["}

        for bracket in s:
            if bracket in brackets:
                if stack and stack[-1]==brackets[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        if not stack:
            return True
        else:
            return False