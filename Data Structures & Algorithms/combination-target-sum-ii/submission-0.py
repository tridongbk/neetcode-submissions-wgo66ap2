class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, path, total):
            # TODO: base case
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            # TODO: loop
            for i in range(start, len(candidates)):
                # TODO: skip duplicate
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                # TODO: choose
                path.append(candidates[i])
                # TODO: explore
                backtrack(i + 1, path, total + candidates[i])
                # TODO: un-choose
                path.pop()

        backtrack(0, [], 0)
        return res
        