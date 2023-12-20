class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        is_positive = s[0] == "+"
        is_negative = s[0] == "-"
        iterator = is_negative or is_positive
        result = 0
        while iterator < len(s) and s[iterator].isdigit():
            result = result * 10 + int(s[iterator])
            iterator += 1
        result *= -1 if is_negative else 1
        result = 2147483647 if result > 2147483647 else result
        result = -2147483648 if result < -2147483648 else result
        return result
