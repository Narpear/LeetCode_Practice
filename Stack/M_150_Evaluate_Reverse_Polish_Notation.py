from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        intermediates = []
        operators = ['+', '-', '*', '/']

        for character in tokens:
            if character not in operators:
                intermediates.append(int(character))
            else:
                operand2 = intermediates.pop()
                operand1 = intermediates.pop()
                result = 0
                if character=='+':
                    result = operand1 + operand2
                elif character=='-':
                    result = operand1 - operand2
                elif character=='*':
                    result = operand1 * operand2
                else:
                    if (operand1*operand2>=0):
                        result = operand1//operand2 
                    else:
                        result = -1*(abs(operand1)//abs(operand2))
                intermediates.append(result)     

        return intermediates[-1]