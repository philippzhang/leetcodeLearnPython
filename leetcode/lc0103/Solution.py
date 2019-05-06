from leetcode.base.structure.TreeNode import TreeNode


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = []
        queue = [(root, 0)]
        while queue:
            cur, level = queue.pop(0)
            if cur.left:
                queue.append((cur.left, level + 1))
            if cur.right:
                queue.append((cur.right, level + 1))
            stack.append((cur.val, level))
        res = [[] for _ in range(stack[-1][-1] + 1)]
        for i, j in stack:
            if j % 2 == 0:
                res[j].append(i)
            else:
                res[j].insert(0, i)
        return res
