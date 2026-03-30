class Solution:
    def rob(self, nums: List[int]) -> int:
        # Step 1: nếu chỉ có 1 nhà
        if len(nums) == 1:
            return nums[0]

        # Step 2: hàm phụ xử lý House Robber I
        def rob_line(houses):
            prev2 = 0
            prev1 = 0

            for money in houses:
                # lấy nhà này hoặc bỏ nhà này
                cur = max(prev1, prev2 + money)

                # cập nhật 2 biến
                prev2 = prev1
                prev1 = cur

            return prev1

        # Step 3: 2 trường hợp
        # bỏ nhà cuối
        case1 = rob_line(nums[:-1])

        # bỏ nhà đầu
        case2 = rob_line(nums[1:])

        # Step 4: lấy kết quả lớn hơn
        return max(case1, case2)