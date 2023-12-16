from typing import List
from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        counter_of_target = Counter(chars)
        for word in words:
            including = True
            for key, value in Counter(word).items():
                if key not in counter_of_target or counter_of_target[key] < value:
                    including = False
                    break
            if including:
                count += len(word)
        return count

    # Solution 2


"""     count = 0
        counter_of_target = Counter(chars)
        for word in words:
            if counter_of_target >= Counter(word):
                count += len(word) """


sol = Solution()
sol.countCharacters(["", "", ""], "absca")
