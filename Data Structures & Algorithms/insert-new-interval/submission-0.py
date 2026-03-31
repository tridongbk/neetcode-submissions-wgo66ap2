class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for interval in intervals:

            # Case 1: interval nằm hoàn toàn bên trái
            if interval[1] < newInterval[0]:
                # add interval
                res.append(interval)

            # Case 2: interval nằm hoàn toàn bên phải
            elif interval[0] > newInterval[1]:
                # add newInterval
                # rồi cho newInterval = interval
                res.append(newInterval)
                newInterval = interval

            # Case 3: overlap → merge vào newInterval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        # Step cuối: add newInterval
        res.append(newInterval)

        return res

'''
# Duyệt từng interval:
# - nếu nằm bên trái newInterval -> add luôn
# - nếu overlap -> merge vào newInterval
# - nếu nằm bên phải -> add newInterval trước, rồi tiếp tục
'''
