class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: sort
        intervals.sort(key=lambda x: x[0])

        res = []

        # Step 2: init current
        current = intervals[0]

        # Step 3: duyệt từ interval thứ 2
        for interval in intervals[1:]:
            # Case 1: nếu overlap thì merge
            if interval[0] <= current[1]:
                current[1] = max(current[1], interval[1])

            # Case 2: không overlap
            else:
                res.append(current)
                current = interval
            

        # Step cuối: add current
        res.append(current)

        return res

'''
# Sort theo start
# Duyệt từng interval:
# - nếu overlap -> merge vào current
# - nếu không -> add current, rồi update current
'''
