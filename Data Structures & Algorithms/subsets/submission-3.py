class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        res = []
        stack = []
        def backtrack(i, stack):
            if i >= len(nums):
                res.append(stack[:])
                return res

            stack.append(nums[i])
            backtrack(i + 1, stack)
            stack.pop()
            backtrack(i + 1, stack)

        backtrack(0, stack)

        return res