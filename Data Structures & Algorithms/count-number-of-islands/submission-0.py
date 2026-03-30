class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Step 1: handle edge case (grid rỗng)
        if not grid:
            return 0
        
        # Step 2: lấy số hàng và cột
        rows, cols = len(grid), len(grid[0])
        
        # Step 3: biến đếm số đảo
        islands = 0
        
        
        # Step 4: định nghĩa hàm DFS
        def dfs(r, c):
            # Step 4.1: base case
            # - out of bound
            # - gặp nước ("0")
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == "0"
            ):
                return
            
            # Step 4.2: mark visited (biến land -> water)
            grid[r][c] = "0"
            
            # Step 4.3: đi 4 hướng
            # xuống
            dfs(r + 1, c)
            # lên
            dfs(r - 1, c)
            # phải
            dfs(r, c + 1)
            # trái
            dfs(r, c - 1)
        
        # Step 5: duyệt toàn bộ grid
        for r in range(rows):
            for c in range(cols):
                # Step 5.1: nếu gặp land ("1")
                if grid[r][c] == "1":
                    # Step 5.2: tăng số đảo
                    islands += 1
                    # Step 5.3: gọi DFS để "xóa" đảo
                    dfs(r, c)
        
        # Step 6: return kết quả
        return islands
        