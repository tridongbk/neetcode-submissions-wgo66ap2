"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Step 1: edge case
        if not node:
            return None
        
        # Step 2: hashmap old -> new
        old_to_new = {}
        
        # Step 3: DFS
        def dfs(curr):
            # Step 3.1: nếu đã clone rồi
            if curr in old_to_new:
                return old_to_new[curr]
            
            # Step 3.2: tạo node mới
            copy = Node(curr.val)
            
            # Step 3.3: lưu vào map (QUAN TRỌNG để tránh cycle)
            old_to_new[curr] = copy
            
            # Step 3.4: duyệt neighbors
            for nei in curr.neighbors:
                # Step 3.5: clone neighbor
                cloned_nei = dfs(nei)
                
                # Step 3.6: add vào neighbors của copy
                copy.neighbors.append(cloned_nei)
            
            # Step 3.7: return node clone
            return copy
        
        # Step 4: gọi DFS từ node ban đầu
        return dfs(node)
        