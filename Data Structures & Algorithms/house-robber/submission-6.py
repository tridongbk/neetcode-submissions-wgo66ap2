class Solution:
    def rob(self, nums: List[int]) -> int:
        # Step 1: lấy số phần tử
        n = len(nums) 

        # Step 2: handle edge case
        if n == 1:
            return nums[0]
        
        # Step 3: tạo mảng dp
        # dp[i] = max tiền có thể rob từ 0 → i
        dp = [0] * n
        
        # Step 4: base case
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        
        # Step 5: fill dp từ i = 2 → n-1
        for i in range(2, n):
            # lựa chọn:
            # 1. không rob nhà i → dp[i-1]
            # 2. rob nhà i → nums[i] + dp[i-2]
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            
            
        # Step 6: return kết quả
        return dp[n-1]
        