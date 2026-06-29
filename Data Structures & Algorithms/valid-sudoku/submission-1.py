from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        square = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in rows[i]:
                    return False
                elif board[i][j] in columns[j]:
                    return False
                elif board[i][j] in square[(i//3,j//3)]:
                    return False
                else:
                    rows[i].add(board[i][j])
                    columns[j].add(board[i][j])
                    square[(i//3,j//3)].add(board[i][j])
        return True
            

