class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Step 1: handle edge case
        if not grid:
            return 0
        
        # Step 2: lấy số hàng và cột
        rows, cols = len(grid), len(grid[0])
        
        # Step 3: biến lưu max area
        max_area = 0
        
        
        # Step 4: định nghĩa DFS trả về diện tích
        def dfs(r, c):
            # Step 4.1: base case
            # - out of bound
            # - gặp nước (0)
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0
            ):
                return 0
            
            # Step 4.2: mark visited
            grid[r][c] = 0
            
            # Step 4.3: bắt đầu area = 1 (ô hiện tại)
            area = 1
            
            # Step 4.4: cộng diện tích từ 4 hướng
            # xuống
            area += dfs(r + 1, c)
            # lên
            area += dfs(r - 1, c)
            # phải
            area += dfs(r, c + 1)
            # trái
            area += dfs(r, c - 1)
            
            # Step 4.5: return area
            return area
        
        
        # Step 5: duyệt toàn bộ grid
        for r in range(rows):
            for c in range(cols):
                # Step 5.1: nếu gặp land (1)
                if grid[r][c] == 1:
                    # Step 5.2: gọi DFS để lấy diện tích
                    area = dfs(r, c)
                    # Step 5.3: update max_area
                    max_area = max(max_area, area)
        
        # Step 6: return kết quả
        return max_area
        