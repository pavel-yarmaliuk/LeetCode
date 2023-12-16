from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        max_el = max(nums)
        count = 0
        j = 0

        for i in range(len(nums)):
            while j < len(nums) and count < k:
                count += nums[j] == max_el
                j += 1
            if count >= k:
                ans += len(nums) - j + 1
            count -= nums[i] == max_el

        return ans
