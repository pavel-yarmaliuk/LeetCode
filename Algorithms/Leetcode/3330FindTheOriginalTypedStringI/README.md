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

<h2><a href=https://leetcode.com/problems/find-the-original-typed-string-i/>3330.FindTheOriginalTypedStringI</a><h2>

<ul>
<li><p>Problem Difficulty: $\color[RGB]{0, 184, 163}{\textrm{Easy}}$</p></li>
<li><p>Status: $\color[RGB]{44, 187, 93}{\textrm{Accepted}}$</strong></p>
</ul>

<h2>Problem Condition</h2>
<p>Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and <strong>may</strong> press a key for too long, resulting in a character being typed <strong>multiple</strong> times.</p>

<p>Although Alice tried to focus on her typing, she is aware that she may still have done this <strong>at most</strong> <em>once</em>.</p>

<p>You are given a string <code>word</code>, which represents the <strong>final</strong> output displayed on Alice's screen.</p>

<p>Return the total number of <em>possible</em> original strings that Alice <em>might</em> have intended to type.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = "abbcccc"</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The possible strings are: <code>"abbcccc"</code>, <code>"abbccc"</code>, <code>"abbcc"</code>, <code>"abbc"</code>, and <code>"abcccc"</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = "abcd"</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The only possible string is <code>"abcd"</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = "aaaa"</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 100</code></li>
	<li><code>word</code> consists only of lowercase English letters.</li>
</ul>


<p>&nbsp;</p>
<h2>Solution Intuition</h2>
<p>Letters not ordered by alphabet, so one letter can meet more than once. So let's calculate how much each letter meets before it's changed and when it's changed we will add calculated sum - 1 because the last one letter inclusion will broke additivity of the sequention. In the end add + 1 which represents the full string.</p>

<p>&nbsp;</p>
<h2>Solution Code</h2>

```python
class Solution:
    def possibleStringCount(self, word: str) -> int:
        current_sum = 0
        current_letter = '0'
        ans = 0
        for x in word:
            if x != current_letter:
                ans += current_sum - 1
                current_sum = 1
                current_letter = x
            else:
                current_sum += 1
        return ans + current_sum + 1
```

<p>&nbsp;</p>
<h2>Solution Picture</h2>
<img src="images/screenshot.png" alt="solution">