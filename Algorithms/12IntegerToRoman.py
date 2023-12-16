def integerToRoman(num):
    roman_numbers_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    res = ''
    str_num = str(num)
    if len(str(num)) == 4:
        res += 'M' * int(str_num[0])
        str_num = str_num[1:]
    if len(str_num) == 3:
        if int(str_num[0]) == 4:
            res += 'CD'
        elif int(str_num[0]) == 9:
            res += 'CM'
        elif int(str_num[0]) == 0:
            res += ''
        elif int(str_num[0]) >= 5:
            res += 'D' + 'C' * (int(str_num[0]) - 5)
        elif int(str_num[0]) < 5:
            res += 'C' * (int(str_num[0]))
        str_num = str_num[1:]
    if len(str_num) == 2:
        if int(str_num[0]) == 4:
            res += 'XL'
        elif int(str_num[0]) == 9:
            res += 'XC'
        elif int(str_num[0]) == 0:
            res += ''
        elif int(str_num[0]) >= 5:
            res += 'L' + 'X' * (int(str_num[0]) - 5)
        elif int(str_num[0]) < 5:
            res += 'X' * (int(str_num[0]))
        str_num = str_num[1:]
    if len(str_num) == 1:
        if int(str_num[0]) == 4:
            res += 'IV'
        elif int(str_num[0]) == 9:
            res += 'IX'
        elif int(str_num[0]) == 0:
            res += ''
        elif int(str_num[0]) >= 5:
            res += 'V' + 'I' * (int(str_num[0]) - 5)
        elif int(str_num[0]) < 5:
            res += 'I' * (int(str_num[0]))
        str_num = str_num[1:]
    print(res)

integerToRoman(1994)
integerToRoman(2794)
integerToRoman(3294)
