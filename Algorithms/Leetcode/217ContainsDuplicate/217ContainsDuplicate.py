from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = set()
        for x in nums:
            if x in d:
                return True
            else:
                d.add(x)
        return False
