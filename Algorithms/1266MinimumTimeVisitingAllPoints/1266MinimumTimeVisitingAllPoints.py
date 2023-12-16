from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        final_result = 0
        for i in range(1, len(points)):
            final_result += self.chebyshev_distance(points[i], points[i - 1])
        return final_result

    def chebyshev_distance(
        self, first_point: List[int], second_point: List[int]
    ) -> int:
        return max(
            abs(second_point[0] - first_point[0]), abs(second_point[1] - first_point[1])
        )
