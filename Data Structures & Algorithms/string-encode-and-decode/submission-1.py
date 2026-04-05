class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += f"#{len(word)}:{word}"  # Added ':' delimiter
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            if s[i] == '#':
                # Find the length delimiter
                colon_idx = s.find(':', i)
                # Extract the length as integer
                length = int(s[i+1:colon_idx])
                # Extract the word
                word = s[colon_idx+1:colon_idx+1+length]
                res.append(word)
                # Update index to skip past this word
                i = colon_idx + 1 + length
            else:
                break
                
        return res