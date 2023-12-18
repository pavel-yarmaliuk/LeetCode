from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min_number = prev_min = 1000000
        max_number = prev_max = -1
        for x in nums:
            if x <= min_number:
                if min_number < prev_min:
                    prev_min = min_number
                min_number = x
            if x > min_number and x < prev_min:
                prev_min = x
            if x >= max_number:
                if max_number > prev_max:
                    prev_max = max_number
                max_number = x
            if x < max_number and x > prev_max:
                prev_max = x
        return max_number * prev_max - min_number * prev_min
