# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 1️⃣ edge case
        if not root:
            return []
        
        # 2️⃣ init queue + result
        queue = deque([root])
        result = []
        
        # 3️⃣ BFS
        
        while queue:
            
            level = []
            
            # 4️⃣ loop qua từng node trong level
            for _ in range(len(queue)):
            
                # lấy node
                node = queue.popleft()
                
                # add value vào level
                level.append(node.val)
                
                # push children vào queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # 5️⃣ add level vào result
            result.append(level)
        
        return result