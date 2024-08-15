from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for money in bills:
            if money == 5:
                fives += 1
                continue
            if money == 10:
                tens += 1
            
            change = money - 5            
            if change == 5:
                if fives>0:
                    fives -= 1
                    continue
                else:
                    return False

            if change == 15:
                if tens>0 and fives>0:
                    tens -= 1
                    fives -= 1
                    continue
                elif fives>=3:
                    fives -= 3
                    continue
                else:
                    return False

        return True