class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf") for _ in range(len(nums))]
        dp[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= len(nums) - 1:
                dp[i] = 1
                continue
            else:
                tmp = float("inf")
                for j in range(1, nums[i] + 1):
                    if i + j < len(nums):
                        tmp = min(tmp, dp[i + j])

                if tmp != float("inf"):
                    dp[i] = tmp + 1
            
        return dp[0]