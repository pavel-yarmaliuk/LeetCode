from typing import List
from collections import Counter, defaultdict


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        max_el = max(nums)
        count = self.count_max_elements_count(nums, max_el)
        for i in range(len(nums)):
            if count >= k:
                ans += len(nums) - i
            if nums[i] == max_el:
                count -= 1
        return ans

    def count_max_elements_count(self, nums, max_el):
        counter = Counter(nums)
        return counter[max_el]


sol = Solution()
print(
    sol.countSubarrays(
        [
            28,
            5,
            58,
            91,
            24,
            91,
            53,
            9,
            48,
            85,
            16,
            70,
            91,
            91,
            47,
            91,
            61,
            4,
            54,
            61,
            49,
        ],
        1,
    )
)
