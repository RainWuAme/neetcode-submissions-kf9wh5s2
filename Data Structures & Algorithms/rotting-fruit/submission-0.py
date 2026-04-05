class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        def rot(r, c):
            nonlocal fresh
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                grid[r][c] == 0 or grid[r][c] == 2):
                return
            q.append((r, c))
            fresh -= 1
            grid[r][c] = 2

        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        t = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                rot(r + 1, c)
                rot(r - 1, c)
                rot(r, c + 1)
                rot(r, c - 1)
            t += 1

        return t if fresh == 0 else -1
