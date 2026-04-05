class Solution:
    def rob(self, nums: List[int]) -> int:
        max1, max2 = 0, nums[0]

        for i in range(1, len(nums)):
            cur = nums[i]
            tmp = max2
            max2 = max(max1 + cur, max2)
            max1 = tmp

        return max(max1, max2)