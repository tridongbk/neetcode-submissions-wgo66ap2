class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        # Biến quan trọng
        # total → tổng toàn bộ (để check có solution không)
        # tank → xăng hiện tại khi đang đi
        # start → vị trí bắt đầu
        total = 0
        tank = 0
        start = 0

        # Duyệt từ trái sang phải
        for i in range (0, len(gas)-1):
            diff = gas[i] - cost[i]
            tank += diff
            total += diff
            # Điều kiện reset start
            if tank < 0:
                start = i + 1
                tank = 0

        return start

'''
# Greedy:
# - nếu tank < 0 → reset start
# - vì đoạn trước không thể là start hợp lệ
# - nếu tổng >= 0 → luôn có đáp án
'''
