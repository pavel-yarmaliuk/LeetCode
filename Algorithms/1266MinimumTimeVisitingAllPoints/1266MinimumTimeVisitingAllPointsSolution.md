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

<h2><a href="https://leetcode.com/problems/minimum-time-visiting-all-points">1266.MinimumTimeVisitingAllPoints</a><h2>

<ul>
<li><p>Problem Difficulty: $\color[RGB]{0, 184, 163}{\textrm{Easy}}$</p></li>
<li><p>Status: $\color[RGB]{44, 187, 93}{\textrm{Accepted}}$</strong></p>
</ul>

<h2>Problem Condition</h2>

On a 2D plane, there are n points with integer coordinates <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

* In 1 second, you can either:
    * move vertically by one unit,
    * move horizontally by one unit, or
    * move diagonally ```sqrt(2)``` units (in other words, move one unit vertically then one unit horizontally in 1 second).
* You have to visit the points in the same order as they appear in the array.
* You are allowed to pass through points that appear later in the order, but these do not count as visits.

[Decart image](https://assets.leetcode.com/uploads/2019/11/14/1626_example_1.PNG)

<p>&nbsp;</p>
<h2>Examples</h2>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> points = [[1,1],[3,4],[-1,0]]
<strong>Output:</strong> 7
<strong>Explanation:</strong> One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> points = [[3,2],[-2,2]]
<strong>Output:</strong> 5
</pre>

<p>&nbsp;</p>
<h2>Constraints</h2>
<ul>
	<li><code>points.length == n</code></li>
	<li><code>1 <= n <= 100</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-1000 <= points[i][0], points[i][1] <= 1000</code></li> 
    </ul>

<p>&nbsp;</p>
<h2>Solution Intuition</h2>

We can move as a King in chess, so let's use Chebyshev distance for calculating maximal wasted time for moving from point A to point B.
Formula for Chebyshev distance will be like:
```max(abs(second_point.x - first_point.x), abs(second_point.y - first_point.y))```
Then we will go through whole array and calculate Chebyshev distance for ```i``` and ```i - 1``` elements and add distance to result variable.
Iterationg starts from ```1```.
<p>&nbsp;</p>
<h2>Solution Code</h2>

```python
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        final_result = 0
        for i in range(1, len(points)):
            final_result += self.chebyshev_distance(points[i], points[i - 1])
        return final_result

    def chebyshev_distance(
        self, first_point: List[int], second_point: List[int]
    ) -> int:
        return max(
            abs(second_point[0] - first_point[0]), 
            abs(second_point[1] - first_point[1])
        )
```

