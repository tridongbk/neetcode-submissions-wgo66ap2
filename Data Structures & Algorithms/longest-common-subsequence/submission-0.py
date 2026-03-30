class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Step 1: lấy độ dài 2 chuỗi
        m = len(text1)
        n = len(text2)

        # Step 2: tạo bảng dp (m+1) x (n+1)
        # dp[i][j] = LCS của text1[:i] và text2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Step 3: fill bảng
        for i in range(1, m+1):
            for j in range(1, n+1):
                # nếu 2 ký tự hiện tại giống nhau
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]

                # nếu khác nhau
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Step 4: return kết quả cuối
        return dp[m][n]
        
        '''
        so sánh từng cặp ký tự, 
            nếu giống thì +1, 
            nếu không thì lấy max của bỏ 1 bên
        '''