import collections
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r:int , c:int ) -> int:
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            area = 1

            while q:
                row, col = q.popleft()
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr, nc = row+dr, col+dc
                    if 0<=nr<rows and 0<=nc<cols and (nr, nc) not in visited and grid[nr][nc]==1:
                        area += 1
                        q.append((nr, nc))
                        visited.add((nr, nc))
            return area

        
        for r in range(rows):
            for c in range(cols):
                if ((r, c) not in visited and grid[r][c] == 1):
                    area = bfs(r, c)
                    max_area = max(max_area, area)
        
        return max_area