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

<h2><a href=https://leetcode.com/problems/valid-anagram/description/>242.ValidAnagram</a><h2>

<ul>
<li><p>Problem Difficulty: $\color[RGB]{44,187,93}{\textrm{Easy}}$</p></li>
<li><p>Status: $\color[RGB]{44, 187, 93}{\textrm{Accepted}}$</strong></p>
</ul>

<h2>Problem Condition</h2>
<p>Given two strings s and t, return true if t is an <a  href="/dictionary.md#Anagram">anagram</a> of s, and false otherwise.
</p>

<p>&nbsp;</p>
<h2>Examples</h2>
<p><strong class="example">Example 1: </strong></p>

<pre><strong>Input: s = "anagram", t = "nagaram"</strong> 
<strong>Output: true</strong> 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input: s = "rat", t = "car"</strong> 
<strong>Output: false</strong> 
</pre>

<p>&nbsp;</p>
<h2>Constraints</h2>
<ul>
	<li><code>1 <= s.length, t.length <= 5 * 10^4</code></li>
	<li><code>s and t consist of lowercase English letters.</code></li>

</ul>

<p>&nbsp;</p>
<h2>Solution Intuition</h2>
<p>We can create hashmap for all words inside input by counting all letters. After that we can compare this hashmaps and if there are the same, then we return true, else we return false.</p>

<p>&nbsp;</p>
<h2>Solution Code</h2>

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```

<p>&nbsp;</p>
<h2>Solution Picture</h2>
<img src="images/screenshot.png" alt="solution">