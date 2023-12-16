from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot_index = self.search_k(nums)
        left_part_index = self.bin_search(nums[:pivot_index], target)
        right_part_index = self.bin_search(nums[pivot_index:], target)
        if left_part_index >= 0:
            return left_part_index
        if right_part_index >= 0:
            return right_part_index + len(nums[:pivot_index])
        return -1
    def bin_search(self, nums, target) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def search_k(self, nums:List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while r - l > 1:
            mid = (l + r) // 2
            if nums[mid] < nums[l]:
                r = mid
            else:
                l = mid
        return r

sol = Solution()
print(sol.search(nums = [4,5,6,7,0,1,2], target = 0))
print(sol.search(nums = [4,5,0,1,2], target = 3))
print(sol.search(nums = [1], target = 0))
