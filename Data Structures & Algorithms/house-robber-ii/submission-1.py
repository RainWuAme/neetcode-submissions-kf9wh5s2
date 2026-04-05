from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge cases: 空列表或只有一間房
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # 情況 1: 搶第一間到倒數第二間 (忽略最後一間)
        # 情況 2: 搶第二間到最後一間 (忽略第一間)
        max1 = self.rob_linear(nums[:-1])
        max2 = self.rob_linear(nums[1:])
        
        return max(max1, max2)

    def rob_linear(self, nums: List[int]) -> int:
        # 如果切片後是空的，回傳 0
        if not nums:
            return 0
            
        prev_max = 0  # 相當於 dp[i-2]
        curr_max = 0  # 相當於 dp[i-1]

        for num in nums:
            # 決定要不要搶當前這間房
            temp = curr_max
            curr_max = max(prev_max + num, curr_max)
            prev_max = temp
        
        return curr_max