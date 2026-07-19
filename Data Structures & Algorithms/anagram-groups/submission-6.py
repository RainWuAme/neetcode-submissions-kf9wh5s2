class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ord_map = defaultdict(list)
        for word in strs:
            tmp = [0] * 26
            for i in range(len(word)):
                tmp[ord(word[i]) - ord('a')] += 1

            ord_map[tuple(tmp)].append(word)

        return list(ord_map.values())