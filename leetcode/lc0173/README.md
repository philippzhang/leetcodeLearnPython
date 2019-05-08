# [173. Binary Search Tree Iterator][enTitle]

**Medium**

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling  *next()*  will return the next smallest number in the BST.





**Example:**

![img](https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png)

```
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false

```



Note:

-  *next()*  and  *hasNext()*  should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
- You may assume that  *next()*  call will always be valid, that is, there will be at least a next smallest number in the BST when  *next()*  is called.
# [173. 二叉搜索树迭代器][cnTitle]

**中等**

实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用  *next()*  将返回二叉搜索树中的下一个最小的数。



**示例：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/25/bst-tree.png)

```
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // 返回 3
iterator.next();    // 返回 7
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 9
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 15
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 20
iterator.hasNext(); // 返回 false
```



**提示：**

-  *next()*  和  *hasNext()*  操作的时间复杂度是 O(1)，并使用 O( *h* ) 内存，其中  *h* 是树的高度。
- 你可以假设  *next()*  调用总是有效的，也就是说，当调用  *next()*  时，BST 中至少存在一个下一个最小的数。


# 算法思路

# 测试用例
```
173. Binary Search Tree Iterator 173. 二叉搜索树迭代器 Medium
Main.funcListTest
---
["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]
[[[7,3,15,null,null,9,20]],[null],[null],[null],[null],[null],[null],[null],[null],[null]]

=[null,3,7,true,9,true,15,true,20,false]
```

[enTitle]: https://leetcode.com/problems/binary-search-tree-iterator/
[cnTitle]: https://leetcode-cn.com/problems/binary-search-tree-iterator/
