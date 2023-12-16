from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        self.findMaxSubarray(nums, 0, len(nums))
    
    def findMaxSubarray(self, nums, low, high):
        if low == high:
            return (low, high, nums[i])
        mid = (low + high) // 2
        left = self.findMaxSubarray(nums, low, mid)
        right = self.findMaxSubarray(nums, mid + 1, high)
        cross = self.findMaxCrossingSubarray(nums, low, high, mid)
        if left[2] > right[2] and left[2] > cross[2]:
            return left[2]
        if right[2] > cross[2]:
            return right[2]
        return cross[2]

    def findMaxCrossingSubarray(self, nums, low, high, mid):
        left_sum = -99999999999999999999
        sum = 0
        left_max = mid
        for i in range(mid, low - 1, -1):
            sum += nums[i]
            if sum > left_sum:
                left_sum = sum
                left_max = i
        right_sum = -99999999999999999999
        sum = 0
        right_max = mid + 1
        for i in range(mid + 1, high):
            sum += nums[i]
            if sum > right_sum:
                right_sum = sum
                right_max = i
        return left_max, right_max, right_sum + left_sum
