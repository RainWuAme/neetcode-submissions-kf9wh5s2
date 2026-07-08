class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.searchBound(nums, target, True)
        right = self.searchBound(nums, target, False)
        return [left, right]

    def searchBound(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                i = mid
                if leftBias:
                    r = i - 1
                else:
                    l = i + 1

        return i