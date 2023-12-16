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

<h2><a href="https://leetcode.com/problems/find-words-that-can-be-formed-by-characters">1160.FindWordsThatCanBeFormedbyCharacters</a><h2>

<ul>
<li><p>Problem Difficulty: $\color[RGB]{0, 184, 163}{\textrm{Easy}}$</p></li>
<li><p>Status: $\color[RGB]{44, 187, 93}{\textrm{Accepted}}$</strong></p>
</ul>

<h2>Problem Condition</h2>

You are given an array of strings ```words``` and a string ```chars```.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

<p>&nbsp;</p>
<h2>Examples</h2>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> words = ["cat","bt","hat","tree"], chars = "atach"
<strong>Output:</strong> 6
<strong>Explanation:</strong> The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6. 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> words = ["hello","world","leetcode"], chars = "welldonehoneyr"
<strong>Output:</strong> 10
<strong>Explanation:</strong> The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
</pre>

<p>&nbsp;</p>
<h2>Constraints</h2>
<ul>
	<li><code>1 <= words.length <= 1000</code></li>
	<li><code>1 <= words[i].length, chars.length <= 100</code></li>
	<li><code>words[i] and chars consist of lowercase English letters.</code></li>
</ul>

<p>&nbsp;</p>
<h2>Solution Intuition</h2>


You need to find count of each ```char``` in ```chars``` string. After that you should go through all words in ```words``` 
array and check by each char from counted chars in word: is the number of particular character in word lower than count of character in chars.

<p>&nbsp;</p>
<h2>Solution Code</h2>

```python
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        counter_of_target = Counter(chars)
        for word in words:
            if counter_of_target >= Counter(word):
                count += len(word)
        return count
```

