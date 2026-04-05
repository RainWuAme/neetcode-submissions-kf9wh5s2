class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memory = set()
        result = 0
        l = 0
        for c in s:
            if c not in memory:
                memory.add(c)
            else:
                result = max(result, len(memory))
                while c in memory:
                    memory.remove(s[l])
                    l += 1
                memory.add(c)
            result = max(result, len(memory))
        return result