<!-- <style>

.hard{
    color: rgb(255 55 95)
}

.medium{
    color: rgb(255 192 30)
}

.easy{
    color: rgb(0 184 163)
}

.accepted{
    color: rgb(44 187 93)
}

.error{
    color:rgb(239 71 67)
}

</style> -->

<h2><a href="https://leetcode.com/problems/longest-consecutive-sequence">128.LongestConsecutiveSequence</a><h2>

<ul>
<li><p>Problem Difficulty: $\color[RGB]{255,192, 30}{\textrm{Medium}}$</p></li>
<li><p>Status: $\color[RGB]{44, 187, 93}{\textrm{Accepted}}$</strong></p>
</ul>

<h2>Problem Condition</h2>
<div class="xFUwe" data-track-load="description_content"><p>Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest consecutive elements sequence.</em></p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time.</p>

<p>&nbsp;</p>
<h2>Examples</h2>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [100,4,200,1,3,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest consecutive elements sequence is <code>[1, 2, 3, 4]</code>. Therefore its length is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,3,7,2,5,8,4,6,0,1]
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>
<p>&nbsp;</p>
<h2>Solution</h2>

Let's create a union find structure with ranks based on count of nodes of particular tree. Then we will go through set of ```nums``` and check if
```current_num - 1``` in UnionFind. If yes, then we should ```union``` ```current_num``` and ```current_num - 1``` in one set and update ranks.
After going through all set we will have fully build UnionFind structure. If we will go thourgh all ranks and find maximum rank, we will find answer for the task.
Code complexity will be <code>O(N*log<sup> * </sup>(N))</code> which is super near to O(N). Space complexity will be O(2*N).

<p>&nbsp;</p>
<h2>Solution Code</h2>

```python
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
```

