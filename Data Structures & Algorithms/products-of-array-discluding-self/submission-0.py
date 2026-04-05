class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        prefixs = [prefix]
        suffixs = [suffix]
        for i in range(1, len(nums)):
            prefix = prefix*nums[i-1]
            prefixs.append(prefix)
        for j in range(len(nums)-2, -1, -1):
            suffix = suffix*nums[j+1]
            suffixs.append(suffix)

        res = []
        for k in range(len(prefixs)):
            res.append(prefixs[k]*suffixs[-k-1])

        return res
