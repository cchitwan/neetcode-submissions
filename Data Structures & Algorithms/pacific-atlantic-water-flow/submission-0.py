class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()


        def dfs(r, c, visited, prev_height):
            if r<0 or r >= rows or c<0 or c >= cols or heights[r][c] < prev_height or (r,c) in visited:
                return
            visited.add((r,c))
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                dfs(r+dr, c+dc, visited, heights[r][c])  

        for i in range(rows):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, cols-1, atlantic, heights[i][cols-1])

        for i in range(cols):
            dfs(0, i, pacific, heights[0][i])
            dfs(rows-1, i, atlantic, heights[rows-1][i])  

        return list(pacific.intersection(atlantic))        


