from collections import deque

INF = 2147483647

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Step 1: handle edge case
        if grid is None:
            return
        
        # Step 2: lấy số hàng, số cột
        rows = len(grid)
        cols = len(grid[0])
        
        # Step 3: tạo queue cho BFS
        queue = deque()
        
        # Step 4: duyệt toàn bộ grid
        # ô nào là treasure (0) thì cho vào queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        # Step 5: tạo 4 hướng di chuyển xuo
        directions = [
            (1, 0),   # xuống
            (-1, 0),  # lên
            (0, 1),   # phải
            (0, -1)   # trái
        ]
        
        # Step 6: BFS từ tất cả treasure cùng lúc
        while queue:
            # lấy ô hiện tại ra
            r, c = queue.popleft()
            
            # duyệt 4 hướng
            for dr, dc in directions:
                # tính tọa độ mới
                nr = r + dr
                nc = c + dc
                
                # Step 6.1: nếu out of bounds thì bỏ qua
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                
                # Step 6.2: nếu không phải ô INF thì bỏ qua
                # (vì -1, 0, hay ô đã update rồi đều không cần đi tiếp)
                if grid[nr][nc] != INF:
                    continue
                
                # Step 6.3: update khoảng cách cho ô hàng xóm
                grid[nr][nc] = grid[r][c] + 1
                
                # Step 6.4: đưa ô mới vào queue
                queue.append((nr, nc))
        
        