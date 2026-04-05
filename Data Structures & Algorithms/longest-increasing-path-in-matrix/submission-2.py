class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = [[0] * COLS for _ in range(ROWS)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if memo[r][c] != 0:
                return memo[r][c]

            res = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and
                    matrix[nr][nc] > matrix[r][c]):
                    res = max(res, 1 + dfs(nr, nc))

            memo[r][c] = res
            return res

        max_path = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_path = max(max_path, dfs(r, c))

        return max_path