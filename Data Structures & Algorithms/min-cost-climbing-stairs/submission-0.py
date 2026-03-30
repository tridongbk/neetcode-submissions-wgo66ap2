# Top = vị trí sau phần tử cuối cùng của mảng, ở example 2:
#   index:   0  1  2  3  4  5  6   TOP
#   cost:   [1, 2, 1, 2, 1, 1, 1]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Step 1: lấy số phần tử
        n = len(cost)
        
        
        # Step 2: tạo mảng dp
        # dp[i] = min cost để tới bậc i
        dp = [0] * n
        
        # Step 3: base case
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        
        # Step 4: fill dp từ 2 → n-1
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            
        
        # Step 5: trả kết quả
        # có thể đi từ n-1 hoặc n-2 tới top
        return min(dp[n-1], dp[n-2])
        