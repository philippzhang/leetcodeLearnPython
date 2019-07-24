# [284. Peeking Iterator][enTitle]

**Medium**

Given an Iterator class interface with methods:  *next()*  and  *hasNext()* , design and implement a PeekingIterator that support the  *peek()*  operation -- it essentially peek() at the element that will be returned by the next call to next().

**Example:**

```
Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.
You call next() the final time and it returns 3, the last element.
Calling hasNext() after that should return false.

```

Follow up: How would you extend your design to be generic and work with all types, not just integer?


# [284. 顶端迭代器][cnTitle]

**中等**

给定一个迭代器类的接口，接口包含两个方法：  *next()*  和  *hasNext()* 。设计并实现一个支持  *peek()*  操作的顶端迭代器 -- 其本质就是把原本应由  *next()*  方法返回的元素  *peek()*  出来。

**示例:**

```
假设迭代器被初始化为列表 [1,2,3]。

调用 next()返回 1，得到列表中的第一个元素。
现在调用 peek() 返回 2，下一个元素。在此之后调用 next()仍然返回 2。
最后一次调用 next() 返回 3，末尾元素。在此之后调用 hasNext() 应该返回 false。

```

**进阶：** 你将如何拓展你的设计？使之变得通用化，从而适应所有的类型，而不只是整数型？




# 算法思路

# 测试用例
```
284. Peeking Iterator 284. 顶端迭代器 Medium
Main.funcListTest
---
["PeekingIterator","next","peek","next","next","hasNext"]
[[[1,2,3]],[],[],[],[],[]]

=[null,1,2,2,3,false]
```

[enTitle]: https://leetcode.com/problems/peeking-iterator/
[cnTitle]: https://leetcode-cn.com/problems/peeking-iterator/
