class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            current = nums[i]
            for j in range(i+1, len(nums)):
                next_value = nums[j]
                if current == next_value:
                    return True

        return False
