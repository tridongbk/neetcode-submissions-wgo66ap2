class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Step 1: transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # Step 2: reverse each row
        for row in matrix:
            row.reverse()
        
'''
🧠 Ý tưởng
Bước 1: Transpose (chéo chính)
matrix[i][j] ↔ matrix[j][i]

👉 đổi hàng ↔ cột

Bước 2: Reverse từng hàng

👉 đảo ngược mỗi row

🔍 Ví dụ
Input:
1 2 3
4 5 6
7 8 9
Step 1: Transpose
1 4 7
2 5 8
3 6 9
Step 2: Reverse từng hàng
7 4 1
8 5 2
9 6 3

👉 Done ✅
'''