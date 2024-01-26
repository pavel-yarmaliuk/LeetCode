class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def calculate(x, y, moves):
            if x < 0 or y < 0 or x >= m or y >= n:
                return 1
            if moves == maxMove:
                return 0
            ans = 0
            ans += calculate(x + 1, y, moves + 1)
            ans += calculate(x, y + 1, moves + 1)
            ans += calculate(x - 1, y, moves + 1)
            ans += calculate(x, y - 1, moves + 1)
            return ans % 1000000007
        return calculate(startRow, startColumn, 0)
        