class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = [[False]*cols for _ in range(rows)]

        def dfs(i, j):
            if 0<=i< rows and 0<=j<cols:
                if grid[i][j] == '1' and not visited[i][j]:
                    visited[i][j] = True
                    for dr, dc in [[1,0], [0,1], [-1,0], [0, -1]]:
                        dfs(i+dr, j+dc) 

        total_island = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    total_island += 1

        return total_island            

        