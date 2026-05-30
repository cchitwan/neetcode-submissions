class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        uncapturable = set()

        visited = [[0] * cols for _ in range(rows)]

        def dfs(i,j, visited, uncapturable):
            if 0<=i<rows and 0<=j<cols and not visited[i][j] and board[i][j] == 'O':
                visited[i][j] = 1
                uncapturable.add((i,j))
                for dr, dc in [[1,0], [0,1], [-1, 0], [0, -1]]:
                    dfs(i+dr, j+dc, visited, uncapturable)

        for i in range(rows):
            dfs(i,0, visited, uncapturable)
            dfs(i,cols-1, visited, uncapturable) 

        for j in range(cols):
            dfs(0,j, visited, uncapturable)
            dfs(rows-1,j, visited, uncapturable)               

        for i in range(rows):
            for j in range(cols):
                if (i,j) not in uncapturable and board[i][j] == 'O':
                    board[i][j] = 'X'  
                    

        