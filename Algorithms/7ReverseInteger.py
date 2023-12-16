class Solution:
    def reverse(self, x: int) -> int:
        multiplier = 1
        if x < 0:
            multiplier = -1
            x = abs(x)
        x = int(str(x)[::-1]) * multiplier
        if -2147483648 <= x <= 2147483647:
            return x
        else:
            return 0
