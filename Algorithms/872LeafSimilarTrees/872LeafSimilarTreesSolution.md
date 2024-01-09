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

<h2><a href="https://leetcode.com/problems/leaf-similar-trees">872.LeafSimilarTrees</a><h2>

<ul>
<li><p>Problem Difficulty: $\color[RGB]{0, 184, 163}{\textrm{Easy}}$</p></li>
<li><p>Status: $\color[RGB]{44, 187, 93}{\textrm{Accepted}}$</strong></p>
</ul>

<h2>Problem Condition</h2>
<p>Condition</p>

<p>&nbsp;</p>
<div class="px-5 pt-4"><div class="flex"></div><div class="xFUwe" data-track-load="description_content"><p>Consider all the leaves of a binary tree, from&nbsp;left to right order, the values of those&nbsp;leaves form a <strong>leaf value sequence</strong><em>.</em></p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png" style="width: 400px; height: 336px;"></p>

<p>For example, in the given tree above, the leaf value sequence is <code>(6, 7, 4, 9, 8)</code>.</p>

<p>Two binary trees are considered <em>leaf-similar</em>&nbsp;if their leaf value sequence is the same.</p>

<p>Return <code>true</code> if and only if the two given trees with head nodes <code>root1</code> and <code>root2</code> are leaf-similar.</p>

<p>&nbsp;</p>
<h2>Examples</h2>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg" style="width: 600px; height: 237px;">
<pre><strong>Input:</strong> root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg" style="width: 300px; height: 110px;">
<pre><strong>Input:</strong> root1 = [1,2,3], root2 = [1,3,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in each tree will be in the range <code>[1, 200]</code>.</li>
	<li>Both of the given trees will have values in the range <code>[0, 200]</code>.</li>
</ul>
</div></div>

<p>&nbsp;</p>
<h2>Solution Intuition</h2>

Default DFS problem. We should recursively iterate until current node valid and have childs.
Order of DFS is next: firstly we generating values from left sub-tree using ```yield from``` operator (used 
for returning values from other generator, since we are using recursion, we need use ```yield from``` instead of ```yield```), 
after that we returning values from right sub-tree. In the end we are comparing final lists from first tree and second tree.

<p>&nbsp;</p>
<h2>Solution Code</h2>

```python
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode],
                    root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root:
                if not root.left and not root.right:
                    yield root.val
                yield from dfs(root.left)
                yield from dfs(root.right)

        return list(dfs(root1)) == list(dfs(root2))
```

