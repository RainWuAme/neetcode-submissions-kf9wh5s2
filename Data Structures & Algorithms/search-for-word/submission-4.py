class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visiting = set()
        def dfs(i, j, target_i):
            if target_i == len(word):
                return True
            if (i < 0 or j < 0 or i >= ROWS or j >= COLS or
                (i, j) in visiting or board[i][j] != word[target_i]):
                return False

            visiting.add((i, j))
            res = dfs(i + 1, j, target_i + 1) or dfs(i - 1, j, target_i + 1) or \
                    dfs(i, j + 1, target_i + 1) or dfs(i, j - 1, target_i + 1)
            visiting.remove((i, j))
            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True

        return False
