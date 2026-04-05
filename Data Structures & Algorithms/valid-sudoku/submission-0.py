class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_checked = {}
        column_checked = {}
        for i in range(len(board)):
            row_checked[i] = set()
            column_checked[i] = set()
        block_checked = {}
        for m in range(3):
            for n in range(3):
                block_checked[(m, n)] = set()
        for i in range(len(board)):
            for j in range(len(board)):
                # Skip empty cells
                if board[i][j] == ".":
                    continue
                number = int(board[i][j])
                if number in row_checked[i]:
                    return False
                else:
                    row_checked[i].add(number)
                if number in column_checked[j]:
                    return False
                else:
                    column_checked[j].add(number)
                current_block_index = (i//3, j//3)
                if number in block_checked[current_block_index]:
                    return False
                else:
                    block_checked[current_block_index].add(number)

        return True

                