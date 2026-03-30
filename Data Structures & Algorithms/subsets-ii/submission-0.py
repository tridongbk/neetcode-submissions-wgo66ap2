class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(start, path):
            # TODO: add subset
            res.append(path[:])
            
            # TODO: loop
            for i in range(start, len(nums)):
                # TODO: skip duplicate
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                # TODO: choose
                path.append(nums[i])
                
                # TODO: explore
                backtrack(i + 1, path)
                
                # TODO: un-choose
                path.pop()

        backtrack(0, [])
        return res
        