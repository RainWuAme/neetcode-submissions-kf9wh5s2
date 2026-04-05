class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_indices = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_indices:
                return [prev_indices[diff], i]
            else:
                prev_indices[num] = i