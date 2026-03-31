class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current_sum = nums[0]
        max_sum = nums[0]

        for i in range (1, len(nums)):
            if current_sum >= 0:
                current_sum = max(nums[i], current_sum + nums[i])
            else:
                current_sum = nums[i]

            max_sum = max(max_sum, current_sum)

        return max_sum

'''
# Ý tưởng (Kadane's Algorithm):
# - Duyệt từng phần tử, tại mỗi vị trí quyết định:
#   + Nối vào subarray trước đó
#   + Hoặc bắt đầu subarray mới từ chính nó
# - Nếu tổng trước đó < 0 thì bỏ, start lại
# - Luôn cập nhật max_sum là kết quả lớn nhất
'''
