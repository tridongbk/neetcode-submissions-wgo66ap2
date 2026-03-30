class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start, path, total):
            # TODO: base case
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            # TODO: loop
            for i in range(start, len(nums)):
                # TODO: choose
                path.append(nums[i])
                # TODO: explore
                backtrack(i, path, total + nums[i])
                # TODO: un-choose
                path.pop()

        backtrack(0, [], 0)
        return res
        