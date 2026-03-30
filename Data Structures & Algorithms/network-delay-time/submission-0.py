import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: build graph (adj list)
        graph = {i: [] for i in range(1, n + 1)}

        for u, v, w in times:
            graph[u].append((v, w))
        
        # Step 2: min heap (time, node)
        heap = [(0, k)]
        
        # Step 3: visited set
        visited = set()
        res = 0
        
        # Step 4: Dijkstra loop
        while heap:
            time, node = heapq.heappop(heap)

            if node in visited:
                continue
            
            visited.add(node)
            res = time

            for nei, w in graph[node]:
                if nei not in visited:
                    heapq.heappush(heap, (time + w, nei))
        
        # Step 5: check result
        return res if len(visited) == n else -1

'''
# Dijkstra:
# luôn đi node có time nhỏ nhất trước
# lần đầu tới node = shortest path
# max shortest path = answer
'''