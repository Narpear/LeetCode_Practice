from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])

        rows = [1]*m
        cols = [1]*n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    cols[j] = 0

        # print("rows: ", rows, "cols: ", cols)

        for i in range(1, m):
            if rows[i] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(n):
            if cols[j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        if rows[0] == 0:
            for i in range(n):
                matrix[0][i] = 0        