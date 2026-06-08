class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [['.'] * n for _ in range(n)]

        cols = set()
        pos_diag = set() #(r+c)
        neg_diag = set() # (r-c)
        res = []
        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])

            for c in range(n):
                if c in cols or r+c in pos_diag or r-c in neg_diag:
                    continue
                board[r][c] = 'Q'
                cols.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                backtrack(r+1)
                cols.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
                board[r][c] = '.'

        backtrack(0)

        return res        





         