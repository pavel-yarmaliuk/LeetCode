from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for anagram in strs:
            sorted_anagram = sorted(anagram)
            anagrams[sorted_anagram].append(anagram)
        return [value for _, value in anagrams]
