import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # max heap (dùng -distance)
        heap = []

        for x, y in points:
            
            # 1. tính distance
            dist = x*x + y*y
            
            # 2. push vào heap
            # lưu (distance, point)
            heapq.heappush(heap, (-dist, x, y))
            
            # 3. giữ size = k
            if len(heap) > k:
                heapq.heappop(heap)
        
        # 4. build kết quả
        res = []
        for dist, x, y in heap:
            res.append([x, y])
        
        return res
        