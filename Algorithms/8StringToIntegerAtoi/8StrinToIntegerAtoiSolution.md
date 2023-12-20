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

<h2><a href="https://leetcode.com/problems/string-to-integer-atoi">8.StrinToIntegerAtoi</a><h2>

<ul>
<li><p>Problem Difficulty: $\color[RGB]{255,192, 30}{\textrm{Medium}}$</p></li>
<li><p>Status: $\color[RGB]{44, 187, 93}{\textrm{Accepted}}$</strong></p>
</ul>

<h2>Problem Condition</h2>
<div class="xFUwe" data-track-load="description_content"><p>Implement the <code>myAtoi(string s)</code> function, which converts a string to a 32-bit signed integer (similar to C/C++'s <code>atoi</code> function).</p>

<p>The algorithm for <code>myAtoi(string s)</code> is as follows:</p>

<ol>
	<li>Read in and ignore any leading whitespace.</li>
	<li>Check if the next character (if not already at the end of the string) is <code>'-'</code> or <code>'+'</code>. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.</li>
	<li>Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.</li>
	<li>Convert these digits into an integer (i.e. <code>"123" -&gt; 123</code>, <code>"0032" -&gt; 32</code>). If no digits were read, then the integer is <code>0</code>. Change the sign as necessary (from step 2).</li>
	<li>If the integer is out of the 32-bit signed integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then clamp the integer so that it remains in the range. Specifically, integers less than <code>-2<sup>31</sup></code> should be clamped to <code>-2<sup>31</sup></code>, and integers greater than <code>2<sup>31</sup> - 1</code> should be clamped to <code>2<sup>31</sup> - 1</code>.</li>
	<li>Return the integer as the final result.</li>
</ol>

<p><strong>Note:</strong></p>

<ul>
	<li>Only the space character <code>' '</code> is considered a whitespace character.</li>
	<li><strong>Do not ignore</strong> any characters other than the leading whitespace or the rest of the string after the digits.</li>
</ul>

<p>&nbsp;</p>
<h2>Examples</h2>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "42"
<strong>Output:</strong> 42
<strong>Explanation:</strong> The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "<u>42</u>" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-2<sup>31</sup>, 2<sup>31</sup> - 1], the final result is 42.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "   -42"
<strong>Output:</strong> -42
<strong>Explanation:</strong>
Step 1: "<u>   </u>-42" (leading whitespace is read and ignored)
            ^
Step 2: "   <u>-</u>42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -<u>42</u>" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-2<sup>31</sup>, 2<sup>31</sup> - 1], the final result is -42.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "4193 with words"
<strong>Output:</strong> 4193
<strong>Explanation:</strong>
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "<u>4193</u> with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-2<sup>31</sup>, 2<sup>31</sup> - 1], the final result is 4193.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 200</code></li>
	<li><code>s</code> consists of English letters (lower-case and upper-case), digits (<code>0-9</code>), <code>' '</code>, <code>'+'</code>, <code>'-'</code>, and <code>'.'</code>.</li>
</ul>
</div>
<p>&nbsp;</p>
<h2>Solution Intuition</h2>
For solve this problem firstly we need to find left and right border. To find left border we need to remove all whitespaces from the string and then 
understand is our number positive or negative (be careful with case when before number input have "-" and "+" like "+-+111") we can do it after finding right border.
Right border we will find from lazy detected left border ```if string[0] == "-" or string[0] == "+"``` then we start from 1 index else we will start from 0 index.
This will continue until ```r < len(s) or string[r].isdigit()``` it means that or we will finish at the end of the string or our current ```s[r]``` will not be a number.
After we founded right border we should finally identify left border by checking first character. Then we should check that value between left and right border is number.
If not return 0 else check that we are not outgoing from Constraints and return result.


<p>&nbsp;</p>
<h2>Solution Code</h2>

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        r = s[0] == "-" or s[0] == "+"
        while r < len(s) and s[r].isdigit():
            r += 1
        positiviness = False
        if len(s[:r]) > 1 and (s[0] == "-" or s[0] == "+"):
            positiviness = True
        if s[positiviness:r].isdigit():
            res = int(s[positiviness:r])
            res = res * (-1) if s[0] == '-' else res
            if res <= 2147483648 - 1 and res >= -2147483648:
                return res
            if res > 2147483648 - 1:
                return 2147483648 - 1
            else:
                return -2147483648
        else:
            return 0
```

