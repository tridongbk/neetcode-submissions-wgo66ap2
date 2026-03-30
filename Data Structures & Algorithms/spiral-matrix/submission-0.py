class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Step 1: init boundaries
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        res = []

        # Step 2: loop while valid boundary
        while top <= bottom and left <= right:

            # Step 3: left → right
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1
            
            # Step 4: top → bottom
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1
            
            # Step 5: right → left
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1
            
            # Step 6: bottom → top
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1
        
        return res

# đi 4 hướng: → ↓ ← ↑
# mỗi lần đi xong → shrink boundary
