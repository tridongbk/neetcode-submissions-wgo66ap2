class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Step 1: sort theo end
        intervals.sort(key=lambda x: x[1])
        print("Sorted:", intervals)

        remove = 0

        # Step 2: init prev_end
        prev_end = intervals[0][1]
        print(f"Start with prev_end = {prev_end}")

        # Step 3: duyệt từ interval thứ 2
        for interval in intervals[1:]:
            print(f"\nChecking interval: {interval}")
            print(f"Compare: {interval[0]} < {prev_end} ?")

            # Case 1: nếu overlap thì xóa interval hiện tại
            if interval[0] < prev_end:
                remove += 1
                print(f"❌ Overlap -> REMOVE {interval}")
                print(f"   prev_end stays = {prev_end}")

            # Case 2: không overlap
            else:
                print(f"✅ No overlap -> KEEP {interval}")
                prev_end = interval[1]
                print(f"   update prev_end = {prev_end}")

        print(f"\nTotal removed: {remove}")
        return remove

'''
# Greedy:
# - sort theo end
# - nếu overlap -> remove++
# - nếu không -> update prev_end
# prev_end = end của interval "đang active"
# mỗi lần KEEP thì cập nhật nó
# mỗi lần REMOVE thì giữ nguyên nó
'''
