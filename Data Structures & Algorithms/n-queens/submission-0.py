class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_set = set()
        positive_set = set()
        negative_set = set()

        res = []
        board = [["."] * n for i in range(n)]
        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in col_set or (r + c) in positive_set or (r - c) in negative_set:
                    continue
                col_set.add(c)
                positive_set.add(r + c)
                negative_set.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col_set.remove(c)
                positive_set.remove(r + c)
                negative_set.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return res
