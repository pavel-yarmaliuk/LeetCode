from typing import List


class UnionFind:
    def __init__(self, nums: List[int]):
        self.unions = {n: n for n in nums}
        self.ranks = {n: 1 for n in nums}

    def union(self, first_set: int, second_set: int):
        first_set_parent = self.get(first_set)
        second_set_parent = self.get(second_set)
        if first_set_parent != second_set_parent:
            if self.ranks[first_set_parent] > self.ranks[second_set_parent]:
                first_set_parent, second_set_parent = (
                    second_set_parent,
                    first_set_parent,
                )
            self.unions[first_set_parent] = second_set_parent
            self.ranks[second_set_parent] += self.ranks[first_set_parent]

    def get(self, set_number: int):
        if set_number != self.unions[set_number]:
            self.unions[set_number] = self.get(self.unions[set_number])
        return self.unions[set_number]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Solution 1
        # nums_set = set(nums)
        # max_sequence_length = 0
        # for x in nums_set:
        #     if (x - 1) not in nums_set:
        #         length = 1
        #         while (x + length) in nums_set:
        #             length += 1
        #         else:
        #             max_sequence_length = max(max_sequence_length, length)
        # return max_sequence_length
        # Solution 2
        uf = UnionFind(nums)
        for n in set(nums):
            if (n - 1) in uf.unions:
                uf.union(n, n - 1)
        return max(uf.ranks.values()) if uf.ranks else 0
