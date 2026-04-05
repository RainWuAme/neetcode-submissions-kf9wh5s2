class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        res = 0
        for num in nums:
            if num-1 in num_set: # Meaning num is not a in the consecutive list start point
                continue
            else:
                step = 1
                tmp_len = 1
                while num+step in num_set:
                    tmp_len += 1
                    step += 1
                res = max(res, tmp_len)
            
        return res
                
        
