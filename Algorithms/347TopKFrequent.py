from typing import List
from random import randint

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_frequent_elements = dict()
        for x in nums:
            if x not in most_frequent_elements:
                most_frequent_elements[x] = 1
            else:
                most_frequent_elements[x] += 1      
        most_frequent_elements_list = list(most_frequent_elements.items())
        index = self.quick_select(most_frequent_elements_list, 0, len(most_frequent_elements_list) - 1, k)
        # sorted_dict = sorted(most_frequent_elements.items(), key = lambda x: x[1], reverse=True)
        # ans = []
        # for key, value in sorted_dict:
        #     if k == 0:
        #         break
        #     ans.append(key)
        #     k -= 1
        return [x[0] for x in most_frequent_elements_list[:index + 1]]
    
    def quick_select(self, nums:List[tuple[int, int]], l:int, r:int, k:int) -> int:
        pivot_index = self.partition(nums, l, r)
        if pivot_index == k - 1:
            return pivot_index
        if pivot_index > k - 1:
            return self.quick_select(nums, l, pivot_index - 1, k)
        return self.quick_select(nums, pivot_index + 1, r, k)
    
    def partition(self, nums:List[tuple[int, int]], l:int, r:int) -> int:
        pivot_index = randint(l, r)
        nums[r], nums[pivot_index] = nums[pivot_index], nums[r]
        pivot = nums[r][1]
        i = l
        for j in range(l, r):
            if nums[j][1] >= pivot:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[r], nums[i] = nums[i], nums[r]
        return i
    
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))
print(sol.topKFrequent([1], 1))