from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency
        count = Counter(nums)
        
        # Step 2: Create buckets
        # index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Step 3: Put numbers into correct bucket
        for num, freq in count.items():
            buckets[freq].append(num)
        
        # Step 4: Collect top k elements
        result = []
        for i in range(len(nums), 0, -1):  # from high freq to low
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result