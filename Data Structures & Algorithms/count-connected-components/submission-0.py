class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node, prev):
            if node in visit:
                return
            visit.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                dfs(nei, node)

        output = 0
        for node in range(n):
            if node in visit:
                continue
            dfs(node, -1)
            output += 1
        
        return output

        