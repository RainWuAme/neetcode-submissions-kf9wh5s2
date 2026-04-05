class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for text in strs:
            sort_text = ''.join(sorted(text))
            if sort_text in groups:
                groups[sort_text].append(text)
            else:
                groups[sort_text] = [text]
        
        return list(groups.values())