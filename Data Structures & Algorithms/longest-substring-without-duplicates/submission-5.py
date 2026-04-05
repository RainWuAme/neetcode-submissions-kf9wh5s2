class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        count = {}
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            if count[s[r]] == 1:
                res = max(res, (r - l + 1))
            else:
                while count[s[r]] > 1:
                    count[s[l]] -= 1
                    l += 1
        return res
