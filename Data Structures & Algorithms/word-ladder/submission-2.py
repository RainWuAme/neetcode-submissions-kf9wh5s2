class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # Build pattern graph
        pattern_graph = defaultdict(list)
        wordList.append(beginWord)
        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] + '*' + w[j+1:]
                pattern_graph[pattern].append(w)

        # Shortest path, bfs
        res = 1
        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for nei in pattern_graph[pattern]:
                        if nei in visited:
                            continue
                        visited.add(nei)   
                        q.append(nei)
            res += 1

        return 0
