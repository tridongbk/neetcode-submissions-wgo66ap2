class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

        return True

'''
# Greedy:
# - farthest = vị trí xa nhất có thể tới
# - nếu i > farthest → không tới được
# - cập nhật farthest = max(farthest, i + nums[i])
'''