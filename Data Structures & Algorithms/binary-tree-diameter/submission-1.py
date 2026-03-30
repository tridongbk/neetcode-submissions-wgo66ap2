# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def dfs(node):
            nonlocal diameter
            
            # 1️⃣ base case
            if not node:
                return 0
            
            # 2️⃣ recursion
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 3️⃣ update global diameter
            diameter = max(diameter, left + right)
            
            # 4️⃣ return depth
            return 1 + max(left, right)
        
        dfs(root)
        return diameter