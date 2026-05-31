class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        ans = 0
        effort = [[math.inf] * cols for _ in range(rows)]
        effort[0][0] = 0

        # (current_effort, row, col)
        min_heap = [(0, 0, 0)] 

        while min_heap:
            curr_effort, r, c = heapq.heappop(min_heap)

            if r == rows-1 and c == cols-1:
                return curr_effort

            if curr_effort > effort[r][c]:
                continue

            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols:
                    new_effort = max(curr_effort, abs(heights[r][c] - heights[nr][nc]))
                    
                    if new_effort < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        heapq.heappush(min_heap, (new_effort, nr, nc))            

        return effort[rows-1][cols-1]