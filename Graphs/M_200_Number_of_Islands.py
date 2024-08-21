import collections
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # base case where the grid is empty and there are no islands
        if not grid:
            return 0

        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            queue = collections.deque([(r, c)])
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == "1" and (r, c) not in visited):
                    islands += 1
                    bfs(r, c)

        return islands
    

# # ALTERNATE DFS FUNCTION
# def bfs(r, c):
#             queue = collections.deque()
#             visited.add((r, c))
#             queue.append((r, c))

#             while queue:
#                 r, c = queue.popleft()
#                 # check [r+1, c]
#                 if r+1<rows and (r+1, c) not in visited and grid[r+1][c] == "1":
#                     queue.append((r+1, c))
#                     visited.add((r+1, c))
#                 # check [r-1, c]
#                 if r-1>=0 and (r-1, c) not in visited and grid[r-1][c] == "1":
#                     queue.append((r-1, c))
#                     visited.add((r-1, c))
#                 # check [r, c+1]
#                 if c+1<cols and (r, c+1) not in visited and grid[r][c+1] == "1":
#                     queue.append((r, c+1))
#                     visited.add((r, c+1))
#                 if c-1>=0 and (r, c-1) not in visited and grid[r][c-1] == "1":
#                     queue.append((r, c-1))
#                     visited.add((r, c-1))