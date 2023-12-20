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

<h2><a href="https://leetcode.com/problems/image-smoother">661.ImageSmoother</a><h2>

<ul>
<li><p>Problem Difficulty: $\color[RGB]{0 184 163}{\textrm{Easy}}$</p></li>
<li><p>Status: $\color[RGB]{44, 187, 93}{\textrm{Accepted}}$</strong></p>
</ul>

<h2>Problem Condition</h2>
<div class="xFUwe" data-track-load="description_content"><p>An <strong>image smoother</strong> is a filter of the size <code>3 x 3</code> that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/smoother-grid.jpg" style="width: 493px; height: 493px;">
<p>Given an <code>m x n</code> integer matrix <code>img</code> representing the grayscale of an image, return <em>the image after applying the smoother on each cell of it</em>.</p>

<p>&nbsp;</p>
<h2>Examples</h2>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/smooth-grid.jpg" style="width: 613px; height: 253px;">

<pre><strong>Input:</strong> img = [[1,1,1],[1,0,1],[1,1,1]]
<strong>Output:</strong> [[0,0,0],[0,0,0],[0,0,0]]
<strong>Explanation:</strong>
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/smooth2-grid.jpg" style="width: 613px; height: 253px;">
<pre><strong>Input:</strong> img = [[100,200,100],[200,50,200],[100,200,100]]
<strong>Output:</strong> [[137,141,137],[141,138,141],[137,141,137]]
<strong>Explanation:</strong>
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == img.length</code></li>
	<li><code>n == img[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= img[i][j] &lt;= 255</code></li>
</ul>
</div>

<p>&nbsp;</p>
<h2>Solution Intuition</h2>

Let's check the index if some of the index equals to 0, then we will not add some of the borders of the frame to the final result.

<p>&nbsp;</p>
<h2>Solution Code</h2>

```python
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row_number = len(img)
        col_number = len(img[0])
        result_arr = [[0]*col_number for _ in range(row_number)]
        for i in range(row_number):
            for j in range(col_number):
                frame = [(i - 1, j - 1), (i, j - 1), (i + 1, j - 1), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1), (i - 1, j), (i + 1, j), (i, j)]
                indexes_not_to_check = set()
                if i == 0:
                    indexes_not_to_check.add(0)
                    indexes_not_to_check.add(3)
                    indexes_not_to_check.add(6)
                if j == 0:
                    indexes_not_to_check.add(0)
                    indexes_not_to_check.add(1)
                    indexes_not_to_check.add(2)
                if i == row_number - 1:
                    indexes_not_to_check.add(2)
                    indexes_not_to_check.add(5)
                    indexes_not_to_check.add(7)
                if j == col_number - 1:
                    indexes_not_to_check.add(3)
                    indexes_not_to_check.add(4)
                    indexes_not_to_check.add(5)
                final_sum_indexes = [img[index_i][index_j] for ind, (index_i, index_j) in enumerate(frame) if ind not in indexes_not_to_check]
                result_arr[i][j] = floor(sum(final_sum_indexes) / len(final_sum_indexes))
        return result_arr
```

