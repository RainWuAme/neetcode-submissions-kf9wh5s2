class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        def add_grid(r, c):
            if (r < 0 or c < 0 or r ==ROWS or c == COLS or
                grid[r][c] == 0 or grid[r][c] == -1 or (r, c) in visited):
                return
            grid[r][c] = dist
            visited.add((r, c))
            q.append((r, c))

        q = deque()
        visited = set()
        dist = 1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                add_grid(r + 1, c)
                add_grid(r - 1, c)
                add_grid(r, c + 1)
                add_grid(r, c - 1)
            dist += 1
