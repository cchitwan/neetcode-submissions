class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        rows, cols = len(grid), len(grid[0])

        visited = [[False] * cols for _ in range(rows)]

        def dfs(i:int, j:int)-> int:
            area = 0
            if 0<=i<rows and 0<=j<cols:
                if grid[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    area = 1
                    for dr, dc in [[1,0], [0,1], [-1, 0], [0, -1]]:
                        area += dfs(i+dr, j+dc)
                    return area
            return area  

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(max_area, dfs(i, j))
                    
        return max_area                          

        