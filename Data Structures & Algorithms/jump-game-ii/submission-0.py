class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        jumps = 0

        while r < len(nums) - 1:
            farthest = 0

            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            jumps += 1

        return jumps

'''
l = biên trái của range hiện tại
r = biên phải của range hiện tại
farthest = vị trí xa nhất có thể tới từ các index trong range đó

# Greedy / BFS-level:
# mỗi lần xét toàn bộ range hiện tại [l..r]
# tìm vị trí xa nhất có thể tới
# sau đó tăng jumps và cập nhật range mới
'''
