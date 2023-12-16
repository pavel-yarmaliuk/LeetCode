class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        s = s.lstrip("+")
        r = len(s) - 1
        while not s[r].isdigit() and r >= 0:
            r -= 1
        is_negative = False
        if len(s[: r + 1]) > 1 and s[0] == "-":
            is_negative = True
        if s[is_negative : r + 1].isdigit():
            res = int(s[is_negative : r + 1])
            res = res * (-1) if is_negative else res
            if res <= 2147483648 - 1 and res >= -2147483648:
                return res
            if res > 2147483648 - 1:
                return 2147483648 - 1
            else:
                return -2147483648
        else:
            return 0


sol = Solution()
print(sol.myAtoi("3.14159265"))
print(sol.myAtoi("42"))
print(sol.myAtoi("   -42"))
print(sol.myAtoi("4193 with words"))
print(sol.myAtoi("-91283472332"))
print(sol.myAtoi("+1"))
print(sol.myAtoi("-4193 with words"))
