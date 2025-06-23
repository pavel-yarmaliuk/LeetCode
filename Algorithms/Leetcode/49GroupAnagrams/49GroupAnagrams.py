from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters_dictionary = {'a': 0,
        'b':0,
        'c':0,
        'd':0,
        'e':0,
        'f':0,
        'g':0,
        'h':0,
        'i':0,
        'j':0,
        'k':0,
        'l':0,
        'm':0,
        'n':0,'o':0, 'p':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0, 'q':0}
        buckets = defaultdict(list)
        for x in strs:
            d = letters_dictionary.copy()
            for c in x:
                d[c] += 1
            key = ""
            for c in d:
                key += f"{c}{d[c]}#"        
            buckets[key].append(x)
        return list(buckets.values())
        
        
