class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, path):
            # TODO: add current subset
            res.append(path[:])
            
            # TODO: loop qua các phần tử còn lại
            for i in range(start, len(nums)):
                # TODO: choose
                path.append(nums[i])
                
                # TODO: explore
                backtrack(i + 1, path)
                
                # TODO: un-choose
                path.pop()
        
        backtrack(0, [])
        return res
        