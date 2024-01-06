from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda x: x[1])
        n = len(jobs)
        dp = [0] * n
        index = 0
        for i in range(n):
            l = -1
            r = i
            while l < r - 1:
                mid = (l + r) // 2
                if jobs[mid][1] <= jobs[i][0]:
                    l = mid
                else:
                    r = mid
            index = l
            dp[i] = max(
                (jobs[i][2] + dp[index]) if index != -1 else jobs[i][2], dp[i - 1]
            )
        return dp[n - 1]
