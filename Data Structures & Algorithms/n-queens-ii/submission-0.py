class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.']* n for _ in range(n)]
        cols= set()
        pos_diag = set()
        neg_diag = set()

        self.ans = 0

        def backtrack(r):
            if r == n:
                self.ans += 1

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

        return self.ans        
