from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        adj = {i:[] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                  x2, y2 = points[j]
                  man_dist = abs(x2-x1) + abs(y2-y1)
                  adj[i].append([man_dist, j])
                  adj[j].append([man_dist, i])

        # Prim's algorithm (greedy)
        res = 0
        visited = set()
        minH = [[0, 0]]     # [cost, point]
        while len(visited) < N:
            cost, i = heapq.heappop(minH)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minH, [neiCost, nei])
        return res