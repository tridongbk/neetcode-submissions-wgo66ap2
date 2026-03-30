import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []

        for num in nums:
            
            # 1. push vào heap
            heapq.heappush(heap, num)
            
            # 2. giữ size = k
            if len(heap) > k:
                heapq.heappop(heap)
        
        # 3. phần tử nhỏ nhất trong heap
        return heap[0]
        