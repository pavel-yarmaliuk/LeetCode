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

<h2><a href="https://leetcode.com/problems/maximum-product-difference-between-two-pairs">1913.MaximumProductDifferenceBetweenTwoPairs</a><h2>

<ul>
<li><p>Problem Difficulty: $\color[RGB]{0, 184, 163}{\textrm{Easy}}$</p></li>
<li><p>Status: $\color[RGB]{44, 187, 93}{\textrm{Accepted}}$</strong></p>
</ul>

<h2>Problem Condition</h2>
<p>The <strong>product difference</strong> between two pairs <code>(a, b)</code> and <code>(c, d)</code> is defined as <code>(a * b) - (c * d)</code>.</p>

<ul>
	<li>For example, the product difference between <code>(5, 6)</code> and <code>(2, 7)</code> is <code>(5 * 6) - (2 * 7) = 16</code>.</li>
</ul>

<p>Given an integer array <code>nums</code>, choose four <strong>distinct</strong> indices <code>w</code>, <code>x</code>, <code>y</code>, and <code>z</code> such that the <strong>product difference</strong> between pairs <code>(nums[w], nums[x])</code> and <code>(nums[y], nums[z])</code> is <strong>maximized</strong>.</p>

<p>Return <em>the <strong>maximum</strong> such product difference</em>.</p>

<p>&nbsp;</p>
<h2>Examples</h2>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [5,6,2,7,4]
<strong>Output:</strong> 34
<strong>Explanation:</strong> We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [4,2,5,9,7,4,8]
<strong>Output:</strong> 64
<strong>Explanation:</strong> We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 * 8) - (2 * 4) = 64.
</pre>

<p>&nbsp;</p>

<h2>Constraints</h2>

<ul>
	<li><code>4 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>
<p>&nbsp;</p>

<h2>Solution Intuition</h2>

First of all we need to see that all numbers are positive, so there are will no be a dificulty that negative number * negative number equals to positive number.
After that we can say that we need to find ```minimal number``` and ```second minimal numbers```,
same for ```maximal``` and ```second maximal number```. After that our result will be ```maximal_number * second_maximal_number - minimal_number * second_minimal_number```.


<p>&nbsp;</p>
<h2>Solution Code</h2>

```python
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min_number = prev_min = 1000000 
        max_number = prev_max = -1
        for x in nums:
            if x <= min_number:
                if min_number < prev_min:
                    prev_min = min_number
                min_number = x
            if x > min_number and x < prev_min:
                prev_min = x
            if x >= max_number:
                if max_number > prev_max:
                    prev_max = max_number
                max_number = x
            if x < max_number and x > prev_max:
                prev_max = x
        return max_number * prev_max - min_number * prev_min
```

