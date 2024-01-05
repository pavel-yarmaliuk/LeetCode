from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(n^2) solution
        # dp = [1] * len(nums)
        # for i in range(len(nums)):
        #    for j in range(i):
        #        if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
        #            dp[i] = dp[j] + 1
        # return max(dp)

        # O(NlogN) solution
        INF = 2**20
        n = len(nums)
        dp = [INF] * (n + 1)
        dp[0] = -INF
        for i in range(n):
            index = bisect_left(dp, nums[i]) + 1
            dp[index] = min(dp[index], nums[i])
        while dp[n] == INF:
            n -= 1
        return n
