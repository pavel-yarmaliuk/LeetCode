from typing import List
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        container = defaultdict(bool)
        for x in nums:
            if x in container:
                return True
            container[x] = True

