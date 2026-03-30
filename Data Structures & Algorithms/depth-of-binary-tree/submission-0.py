# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case
        if not root:
            return 0

        # Call recursion
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # Calculate the depth of node
        return 1 + max(left,right)