class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        nums.sort()
        res = []
        stack = []
        def backtrack(i, stack):
            if sum(stack) == target:
                res.append(stack[:])
                return 
            
            for j in range(i, len(nums)):
                if sum(stack) + nums[j] > target:
                    return
                stack.append(nums[j])
                backtrack(j, stack)
                stack.pop()

        backtrack(0, [])
        return res
            
