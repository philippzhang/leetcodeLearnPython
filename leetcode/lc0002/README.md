# [2. Add Two Numbers]][enTitle]

**Medium**

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```
# [2. 两数相加][cnTitle]

**中等**

给出两个**非空** 的链表用来表示两个非负的整数。其中，它们各自的位数是按照**逆序**的方式存储的，并且它们的每个节点只能存储**一位**数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0开头。

**示例：**

```
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
```

# 算法思路

# 测试用例
```
2. Add Two Numbers 2. 两数相加 Medium
Solution.addTwoNumbers
---
[2,4,3]
[5,6,4]

=[7,0,8]
---
[2,4,3]
[5,6,7,1]

=[7,0,1,2]
```

[enTitle]: https://leetcode.com/problems/add-two-numbers/
[cnTitle]: https://leetcode-cn.com/problems/add-two-numbers/