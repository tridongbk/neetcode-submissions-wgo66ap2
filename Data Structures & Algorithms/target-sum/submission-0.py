class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Step 1: define memo
        memo = {}
        
        # Step 2: define dfs(i, total)
        # i = current index
        # total = current sum
        def dfs(i, total):
            
            # Step 3: base case
            # if reach end of nums
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            
            # Step 4: check memo
            if (i, total) in memo:
                return memo[(i, total)]
            
            # Step 5: choose +
            add = dfs(i+1, total + nums[i])
            
            # Step 6: choose -
            sub = dfs(i+1, total - nums[i])
            
            # Step 7: store result in memo
            memo[(i, total)] = add + sub
            
            # Step 8: return result
            return memo[(i, total)]
        
        # Step 9: start from index 0, total = 0
        return dfs(0, 0)

'''
Target Sum - DFS + Memoization

Idea:
- For each number, we have 2 choices: add (+) or subtract (-)
- Try all possibilities using DFS

State:
- dfs(i, total):
    i     = current index
    total = current sum so far

Transition:
- dfs(i, total) =
    dfs(i+1, total + nums[i]) +
    dfs(i+1, total - nums[i])

Base case:
- If i == len(nums):
    return 1 if total == target else 0

Memoization:
- Use memo[(i, total)] to store computed results
- Avoid recomputing same states

Result:
- Start from dfs(0, 0)

Time Complexity:
- O(n * range of possible sums)

Space Complexity:
- O(n * range) for memo + recursion stack
'''