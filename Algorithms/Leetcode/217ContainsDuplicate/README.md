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

<h2><a href=https://leetcode.com/problems/contains-duplicate/description/>217.ContainsDuplicate</a><h2>

<ul>
<li><p>Problem Difficulty: $\color[RGB]{44,187,93}{\textrm{Easy}}$</p></li>
<li><p>Status: $\color[RGB]{44, 187, 93}{\textrm{Accepted}}$</strong></p>
</ul>

<h2>Problem Condition</h2>
<p>Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.</p>

<p>&nbsp;</p>
<h2>Examples</h2>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input: nums = [1,2,3,1]</strong> 
<strong>Output: true</strong> 
<strong>Explanation: The element 1 occurs at the indices 0 and 3.</strong> 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input: nums = [1,1,1,3,3,4,3,2,4,2]</strong> 
<strong>Output: true</strong> 
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input: nums = [1,2,3,4]</strong> 
<strong>Output: false</strong> 
<strong>Explanation: All elements are distinct.</strong> 
</pre>

<p>&nbsp;</p>
<h2>Constraints</h2>
<ul>
	<li><code>1 <= nums.length <= 10^5</code></li>
	<li><code>-10^9 <= nums[i] <= 10^9</code></li>

</ul>

<p>&nbsp;</p>
<h2>Solution Intuition</h2>
<p>Basicaly creating set to hold only unique items and adding items through iteration by the nums array. If at the iteration we understand that this value already in set - return False</p>

<p>&nbsp;</p>
<h2>Solution Code</h2>

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = set()
        for x in nums:
            if x in d:
                return True
            else:
                d.add(x)
        return False
```

<p>&nbsp;</p>
<h2>Solution Picture</h2>
<img src="images/screenshot.png" alt="solution">