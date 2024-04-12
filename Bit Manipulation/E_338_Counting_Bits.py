class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            count = 0
            j = i
            while j>0:
                count = count + (j%2)
                j = j//2
            result.append(count)

        return result

