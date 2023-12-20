class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        r = s[0] == "-" or s[0] == "+"
        while r < len(s) and s[r].isdigit():
            r += 1
        positiviness = False
        if len(s[:r]) > 1 and (s[0] == "-" or s[0] == "+"):
            positiviness = True
        if s[positiviness:r].isdigit():
            res = int(s[positiviness:r])
            res = res * (-1) if s[0] == "-" else res
            if res <= 2147483648 - 1 and res >= -2147483648:
                return res
            if res > 2147483648 - 1:
                return 2147483648 - 1
            else:
                return -2147483648
        else:
            return 0
