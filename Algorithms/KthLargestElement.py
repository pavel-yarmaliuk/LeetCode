from typing  import List
from random import randint
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, 0, len(nums) - 1, k)

    def quick_select(self, nums, l, r, k):
        pivot_index = self.partition(nums, l, r)
        if pivot_index == k - 1:
            return nums[pivot_index]
        if pivot_index > k - 1:
            return self.quick_select(nums, l, pivot_index - 1, k)
        return self.quick_select(nums, pivot_index + 1, r, k)

    def partition(self, nums, l, r):
        pivot_index = randint(l, r)
        nums[r], nums[pivot_index] = nums[pivot_index], nums[r]
        pivot = nums[r]
        i = l
        for j in range(l, r):
            if nums[j] >= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[r], nums[i] = nums[i], nums[r]
        print(nums)
        return i

    def hoare_partition(self, nums, l, r):
        i = l - 1
        j = r + 1
        pivot = nums[l]
        while True:
            i += 1
            while nums[i] > pivot:
                i += 1
            j -= 1
            while nums[j] < pivot:
                j -= 1
            if i >= j:
                return j
            nums[i], nums[j] = nums[j], nums[i]
sol = Solution()
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
print(sol.findKthLargest([3,2,1,5,6,4], 2))