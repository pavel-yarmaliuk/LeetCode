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

<h2><a href="https://leetcode.com/problems/longest-increasing-subsequence">300.LongestIncreasingSubsequence</a><h2>

<ul>
<li><p>Problem Difficulty: $\color[RGB]{255,192, 30}{\textrm{Medium}}$</p></li>
<li><p>Status: $\color[RGB]{44, 187, 93}{\textrm{Accepted}}$</strong></p>
</ul>

<h2>Problem Condition</h2>
<div class="xFUwe" data-track-load="description_content"><p>Given an integer array <code>nums</code>, return <em>the length of the longest <strong>strictly increasing </strong></em><span data-keyword="subsequence-array" class=" cursor-pointer relative text-dark-blue-s text-sm"><div class="popover-wrapper inline-block" data-headlessui-state=""><div><div aria-expanded="false" data-headlessui-state="" id="headlessui-popover-button-:r2b:"><div><em><strong>subsequence</strong></em></div></div><div style="position: fixed; z-index: 40; inset: 0px auto auto 0px; transform: translate(573px, 222px);"></div></div></div></span>.</p>

<p>&nbsp;</p>

<h2>Examples</h2>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [10,9,2,5,3,7,101,18]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,1,0,3,2,3]
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [7,7,7,7,7,7,7]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2500</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><b>Follow up:</b>&nbsp;Can you come up with an algorithm that runs in&nbsp;<code>O(n log(n))</code> time complexity?</p>
</div>

<p>&nbsp;</p>

<h2>Solution Intuition</h2>

Let's create array of size n + 2 which will store in index ***i*** the ***minmal*** element of the subsequence of length ***i***.
So, it's easy to undersstand, that this array will be strictly increasing. So we can use ***binary search*** to find position, where we should to
insert our new element on each iteration. When we found position, we should to check that this element is lower then current element in this position.
So if it is, we are updating our array. Finally our solution will be stored at maximal index which is not equals to infinity.

<p>&nbsp;</p>
<h2>Solution Code</h2>

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n^2 algorithm
        # dp = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
        #             dp[i] = dp[j] + 1
        # return max(dp)
        INF = 10 ** 5
        n = len(nums)
        dp = [INF] * (n + 2)
        dp[0] = -INF
        for i in range(n):
            index = bisect_left(dp, nums[i])
            dp[index] = min(dp[index], nums[i])
        while dp[n] == INF:
            n -= 1
        return n
```

