import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []

        # TODO: add nums vào heap
        for num in nums:
            # push num vào heap
            heapq.heappush(self.minHeap, num)
            # nếu size > k thì pop
            if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)
            pass
        
    def add(self, val: int) -> int:
        # TODO: thêm val vào heap
        heapq.heappush(self.minHeap, val)
        # TODO: nếu size > k thì pop
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # TODO: return kth largest (phần tử nhỏ nhất trong heap)
        return self.minHeap[0]
        pass
        
    # Notes:
    #   Heap luôn giữ invariant: heap[0] = nhỏ nhất
    #   Nên heappop() sẽ pop phần tử nhỏ nhất ra