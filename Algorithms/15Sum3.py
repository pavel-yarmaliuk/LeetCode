from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        ans = set()
        for i in range(len(sorted_nums)):
            l = i + 1
            r = len(sorted_nums) - 1
            while l < r:
                part_sum = sorted_nums[l] + sorted_nums[r] + sorted_nums[i]
                if part_sum == 0:
                    ans.add(tuple(sorted([sorted_nums[l], sorted_nums[r], sorted_nums[i]])))
                    r -= 1 # Обосновано тем, что для sorted_nums[i] действительная только одна пара sorted_nums[l] и sorted_nums[r], которая бы не повторялась, потому что если мы прибавим только l + 1, то r - 1 всё равно придётся делать, т.к. другой, неповторяющейся пары для sorted_nums[l] не существует.
                    l += 1
                else:
                    if part_sum > 0:
                        r -= 1
                    else:
                        l += 1
        return list(ans)

