from typing import List
class Solution:
    def productExceptSelf(self, nums:List[int]) -> List[int]:
        dpl = [nums[0]]
        dpr = [nums[-1]]
        for i in range(1, len(nums)):
            dpl.append(dpl[i - 1] * nums[i])
            dpr.append(dpr[i - 1] * nums[-(i + 1)])
        ans = [dpr[-2]]
        dpl_index = 0
        dpr_index = len(dpr) - 3
        for i in range(1, len(nums) - 1):
            ans.append(dpl[dpl_index] * dpr[dpr_index])
            dpl_index += 1
            dpr_index -= 1
        ans.append(dpl[-2])
        return ans

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
print(sol.productExceptSelf([-1,1,0,-3,3]))
