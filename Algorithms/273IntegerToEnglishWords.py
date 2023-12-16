
class Solution:
    def numberToWords(self, num: int) -> str:
        degrees = ["Thousand", "Million", "Billion"]
        english_numbers_after_twenty = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
                                        "Eighty", "Ninety"]
        english_numbers = ["One", "Two", "Three", "Four", "Five", "Six", 
                            "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                            "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                            "Eighteen", "Nineteen"]

        ans = ""
        degree_level = 0
        if num == 0:
            return "Zero"
        while num:
            part_of_ans = ""
            write_part = num % 1000
            if write_part >= 100:
                part_of_ans += f"{english_numbers[write_part // 100 - 1]} Hundred "
                write_part %= 100
            if write_part >= 20:
                part_of_ans += f"{english_numbers_after_twenty[write_part // 10 - 2]} "
                write_part %= 10
            if write_part != 0:
                part_of_ans += f"{english_numbers[write_part - 1]} "
            if part_of_ans != "":
                part_of_ans += f"{degrees[degree_level - 1] if degree_level > 0 else ''} " 
            ans = part_of_ans + ans
            degree_level += 1
            num //= 1000 
        return ans.rstrip()

sol = Solution()
print(sol.numberToWords(1000000))
