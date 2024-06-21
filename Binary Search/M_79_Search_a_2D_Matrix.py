from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_number=-1
        m = len(matrix)
        n = len(matrix[0])

        # finding row number
        for i in range(m-1):
            if target>=matrix[i][0] and target<matrix[i+1][0]:
                row_number = i
                break
        if row_number==-1:
            row_number = m-1

        # checking if the number is present in the row or not
        left = 0
        right = n-1
        while(left<=right):
            mid = (left+right)//2
            if matrix[row_number][mid]>target:
                right = mid-1
            elif matrix[row_number][mid]<target:
                left = mid+1
            else:
                if matrix[row_number][mid]==target:
                    return True
        
        return False


