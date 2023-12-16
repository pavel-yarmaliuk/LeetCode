from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Solution 1
        """max_base = len(nums)
        for i in range(len(nums)):
            nums[i] += (nums[nums[i]] % max_base) * max_base
        for i in range(len(nums)):
            nums[i] //= max_base
        return nums
        """
        # Solution 2
        return [nums[nums[i]] for i in range(len(nums))]
