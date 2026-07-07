class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []
        nums.sort()
        def backtrack(i, stack, total):
            if total == target:
                res.append(stack[:])
                return
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                stack.append(nums[j])
                backtrack(j, stack, total + nums[j])
                stack.pop()

        backtrack(0, [], 0)
        return res