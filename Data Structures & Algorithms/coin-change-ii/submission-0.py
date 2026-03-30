class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Step 1: define dp
        # dp[a] = number of combinations to make amount a
        dp = [0]*(amount+1)
        
        # Step 2: base case
        dp[0] = 1
        
        # Step 3: loop through each coin
        for coin in coins:
        
            # Step 4: update all amounts from coin -> amount
            for a in range(coin, amount+1):
                dp[a] += dp[a - coin]
            
        
        # Step 5: return answer
        return dp[amount]
        
        '''
        dp[a] = number of combinations to make amount a

        Base case:
        dp[0] = 1 → there is 1 way to make amount 0 (choose nothing)

        Transition:
        For each coin, update dp from left to right:
        dp[a] += dp[a - coin]

        Meaning:
        - dp[a - coin]: number of ways to make the remaining amount
        - add current coin → forms new ways to make a

        Important:
        - loop coins outside → avoid counting duplicate orders
        - this ensures combinations, not permutations
        '''