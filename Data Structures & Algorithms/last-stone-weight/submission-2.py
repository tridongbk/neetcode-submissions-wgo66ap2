import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # TODO: convert sang max heap (dùng số âm)
        heap = []
        for s in stones:
            heap.append(-s)
        
        # TODO: heapify
        heapq.heapify(heap)

        # TODO: loop đến khi còn <= 1 viên
        while len(heap) > 1:
            
            # lấy 2 viên lớn nhất
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            
            # TODO: nếu khác nhau thì push lại phần dư
            if y != x:
                heapq.heappush(heap, -(y-x))
        
        # TODO: return kết quả
        return -heap[0] if heap else 0
        