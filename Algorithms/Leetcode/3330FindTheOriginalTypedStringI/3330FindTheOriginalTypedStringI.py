class Solution:
    def possibleStringCount(self, word: str) -> int:
        current_sum = 0
        current_letter = '0'
        ans = 0
        for x in word:
            if x != current_letter:
                ans += current_sum - 1
                current_sum = 1
                current_letter = x
            else:
                current_sum += 1
        return ans + current_sum + 1
