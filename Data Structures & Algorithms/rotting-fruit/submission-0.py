from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Step 1: edge case
        if not grid or not grid[0]:
            return 0
        
        # Step 2: lấy rows, cols
        rows = len(grid)
        cols = len(grid[0])

        # Step 3: tạo queue (BFS)
        queue = deque()
        
        # Step 4: đếm số trái tươi + push tất cả trái thối vào queue
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        # Step 5: directions (4 hướng)
        directions = [
            (1, 0),   # xuống
            (-1, 0),  # lên
            (0, 1),   # phải
            (0, -1)   # trái
        ]
        
        # Step 6: BFS theo từng phút
        minutes = 0
        
        while queue and fresh > 0:
            # số phần tử trong layer hiện tại (1 phút)
            size = len(queue)
            
            for _ in range(size):
                # lấy phần tử ra
                r, c = queue.popleft()
                
                # duyệt 4 hướng
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    
                    # Step 6.1: out of bounds
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    
                    # Step 6.2: chỉ xử lý ô tươi (1)
                    if grid[nr][nc] != 1:
                        continue
                    
                    # Step 6.3: làm cho nó bị thối (1 -> 2)
                    grid[nr][nc] = 2
                    
                    # Step 6.4: giảm số trái tươi
                    fresh -= 1
                    
                    # Step 6.5: add vào queue
                    queue.append((nr, nc))
            
            # sau khi xử lý xong 1 layer → tăng phút
            if queue:
                minutes += 1
        
        # Step 7: check kết quả
        # nếu vẫn còn trái tươi → return -1
        # ngược lại → return minutes (có thể cần -1 tùy case)
        if fresh > 0:
            return -1
        else:
            return minutes