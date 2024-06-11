class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checking rows
        for row in board:
            # print(row)
            counts = {}
            for character in row:
                if character=='.':
                    continue
                if character in counts:
                    return False
                counts[character] = 1
            # print(counts)
        
        #checking columns
        for col in range(9):
            counts = {}
            for row in board:
                character = row[col]
                if character=='.':
                    continue
                if character in counts:
                    return False
                counts[character] = 1
            
        #checking mini boxes
        for row in range(0, 9, 3):
            for col in range (0, 9, 3):
                counts = {}
                for i in range(3):
                    for j in range(3):
                        character = board[row+i][col+j]
                        if character=='.':
                            continue
                        if character in counts:
                            return False
                        counts[character] = 1
        
        return True
        
                
            
            
        
