from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed_matrix = []
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(0)
            transposed_matrix.append(row)
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                transposed_matrix[i][j] = matrix[j][i]
        return transposed_matrix


sol = Solution()
sol.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sol.transpose([[1, 2, 3], [4, 5, 6]])
