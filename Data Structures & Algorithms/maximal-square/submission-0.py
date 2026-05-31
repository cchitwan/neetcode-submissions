class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_size = 0 if "1" not in matrix[0] else 1

        if max_size == 0 and "1" in list(zip(*matrix))[0]:
            max_size = 1


        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if int(matrix[i][j]) == 1:
                    matrix[i][j] = str(1 + min(int(matrix[i-1][j-1]), int(matrix[i-1][j]), int(matrix[i][j-1])))
                    max_size = max(max_size, int(matrix[i][j]))


        return max_size ** 2            

        