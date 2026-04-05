class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ord_map = defaultdict(list)

        for s in strs:
            counts = [0]*26
            for alphabet in s:
                counts[ord(alphabet)-ord('a')] += 1
            ord_map[tuple(counts)].append(s)

        return(list(ord_map.values()))
            