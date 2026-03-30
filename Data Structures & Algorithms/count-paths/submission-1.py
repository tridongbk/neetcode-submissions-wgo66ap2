class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Step 1: tạo bảng dp m x n
        dp = [[0] * n for  _ in range(m)]

        # Step 2: fill hàng đầu tiên = 1
        for c in range(n):
            dp[0][c] = 1

        # Step 3: fill cột đầu tiên = 1
        for r in range(m):
            dp[r][0] = 1

        # Step 4: fill các ô còn lại
        for r in range(1, m):
            for c in range(1, n):
                # từ trên + từ trái
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        # Step 5: return ô cuối
        return dp[m-1][n-1]
        
        '''
        Muốn tới (r, c) chỉ có 2 cách:
            từ trên xuống: (r-1, c)
            từ trái sang: (r, c-1)
        '''