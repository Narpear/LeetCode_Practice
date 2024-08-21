from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # create the adjacency list
        adj = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        result = ["JFK"]
        def dfs(src):
            if len(result) == len(tickets)+1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                result.append(v)
                if dfs(v): return True

                adj[src].insert(i, v)
                result.pop()
            return False

        dfs("JFK")
        return result      