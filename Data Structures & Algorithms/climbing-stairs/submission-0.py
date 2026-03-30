class Solution:
    def climbStairs(self, n: int) -> int:
        # Step 1: handle base case
        if n <= 2:
            return n
        
        # Step 2: init dp array
        dp = [0] * (n + 1)
        
        # Step 3: set base values
        dp[1] = 1
        dp[2] = 2
        
        # Step 4: loop to fill dp
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        # Step 5: return result
        return dp[n]