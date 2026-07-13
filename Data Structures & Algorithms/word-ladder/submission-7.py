class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # Build the graph
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)

        # Start finding the shortest path with BFS
        q = deque()
        q.append(beginWord)
        visit = set(beginWord)
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:] 
                    for nei_w in nei[pattern]:
                        if nei_w not in visit:
                            visit.add(nei_w)
                            q.append(nei_w)
                            
            res += 1

        return 0
