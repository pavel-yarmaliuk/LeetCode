from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, x in enumerate(nums):
            if (target - x) in d:
                return [i, d[x]]
            else:
                d[x] = i
      
