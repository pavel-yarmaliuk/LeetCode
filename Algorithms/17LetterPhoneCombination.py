from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.phone_buttons_letters = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        iterations_number = 1 if len(digits) > 0 else 0
        for digit in digits:
            iterations_number *= len(phone_buttons_letters[int(digit)])
        for _ in range(iterations_number):
            for digit in digits:
                
    def findCombindations(self, i, j, digits):
        for digit in digits:
            for letter in self.phone_buttons_letters[int(digit)]:
                pass
