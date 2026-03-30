class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        # Step 1: check if first row has zero
        row_zero = False
        for c in range(cols):
            if matrix[0][c] == 0:
                row_zero = True
        
        # Step 2: check if first col has zero
        col_zero = False
        for r in range(rows):
            if matrix[r][0] == 0:
                col_zero = True

        # Step 3: mark zeros using first row & col
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # Step 4: set inner matrix (exclude first row/col)
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # Step 5: set first row
        if row_zero:
            for c in range(cols):
                matrix[0][c] = 0

        # Step 6: set first column
        if col_zero:
            for r in range(rows):
                matrix[r][0] = 0

'''
🔥 Tóm gọn để nhớ
# use first row & col as markers
# plus 1 variable to track first row
🧠 Insight cực quan trọng
Không được set 0 ngay → sẽ làm “lan sai”
Phải:
mark trước
fill sau
'''
