import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Step 1: init
        n = len(points)
        visited = set()
        heap = [(0, 0)]  # (cost, node_index)
        res = 0
        
        # Step 2: Prim loop
        while len(visited) < n:
            cost, i = heapq.heappop(heap)
            
            if i in visited:
                continue
            
            visited.add(i)
            res += cost
            
            # Step 3: push all neighbors
            for j in range(n):
                if j not in visited:
                    x1, y1 = points[i]
                    x2, y2 = points[j]

                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(heap, (dist, j))
        
        return res

'''
🔥 Tóm gọn để nhớ
# Prim:
# start from 1 node
# always pick smallest edge to new node
# use min heap
'''