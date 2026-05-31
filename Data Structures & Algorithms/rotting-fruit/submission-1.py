class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.deque = deque()

        rows, cols = len(grid), len(grid[0])
        self.fresh_fruit_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    self.deque.append((i,j))
                elif grid[i][j] == 1:
                    self.fresh_fruit_count += 1    

        if self.fresh_fruit_count == 0:
            return 0
        time_taken = 0

        def bfs(i, j):
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                n_i, n_j = i+dr, j+dc
                if 0<=n_i<rows and 0<=n_j<cols and grid[n_i][n_j] == 1:
                    self.deque.append((n_i, n_j))
                    grid[n_i][n_j] = 2
                    self.fresh_fruit_count -= 1
                    

       
        while self.deque and self.fresh_fruit_count>0:
            # print(self.deque, time_taken)
            for _ in range(len(self.deque)):
                r, c = self.deque.popleft()
                bfs(r, c)
            time_taken += 1    

                        

        return -1 if self.fresh_fruit_count > 0 else time_taken



        