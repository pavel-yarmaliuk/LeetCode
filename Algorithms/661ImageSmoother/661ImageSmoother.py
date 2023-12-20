from math import floor


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row_number = len(img)
        col_number = len(img[0])
        result_arr = [[0] * col_number for _ in range(row_number)]
        for i in range(row_number):
            for j in range(col_number):
                frame = [
                    (i - 1, j - 1),
                    (i, j - 1),
                    (i + 1, j - 1),
                    (i - 1, j + 1),
                    (i, j + 1),
                    (i + 1, j + 1),
                    (i - 1, j),
                    (i + 1, j),
                    (i, j),
                ]
                indexes_not_to_check = set()
                if i == 0:
                    indexes_not_to_check.add(0)
                    indexes_not_to_check.add(3)
                    indexes_not_to_check.add(6)
                if j == 0:
                    indexes_not_to_check.add(0)
                    indexes_not_to_check.add(1)
                    indexes_not_to_check.add(2)
                if i == row_number - 1:
                    indexes_not_to_check.add(2)
                    indexes_not_to_check.add(5)
                    indexes_not_to_check.add(7)
                if j == col_number - 1:
                    indexes_not_to_check.add(3)
                    indexes_not_to_check.add(4)
                    indexes_not_to_check.add(5)
                final_sum_indexes = [
                    img[index_i][index_j]
                    for ind, (index_i, index_j) in enumerate(frame)
                    if ind not in indexes_not_to_check
                ]
                result_arr[i][j] = floor(
                    sum(final_sum_indexes) / len(final_sum_indexes)
                )
        return result_arr
