class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows_number = len(grid)
        cols_number = len(grid[0])

        onesRow = [0] * rows_number
        onesCol = [0] * cols_number
        zerosRow = [0] * rows_number
        zerosCol = [0] * cols_number

        for i in range(rows_number):
            for j in range(cols_number):
                if grid[i][j] == 1:
                    onesRow[i] += 1
                    onesCol[j] += 1
                else:
                    zerosRow[i] += 1
                    zerosCol[j] += 1
        diff = [[0] * cols_number for _ in range(rows_number)]
        for i in range(rows_number):
            for j in range(cols_number):
                diff[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
        return diff
