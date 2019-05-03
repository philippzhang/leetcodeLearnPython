
from leetcode.base.Typeassert import typeassert
from leetcode.base.structure.TreeNode import TreeNode


class Solution(object):
    @typeassert(object, TreeNode, rtype=list)
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d = {}

        def helper(node, lv):
            if not node:
                return
            if not lv in d:
                d[lv] = [node.val]
            else:
                d[lv].append(node.val)
            helper(node.left, lv + 1)
            helper(node.right, lv + 1)

        helper(root, 1)
        return [d[x] for x in d]
