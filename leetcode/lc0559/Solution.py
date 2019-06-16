from leetcode.base import PrintObj


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        PrintObj.printObj(root)
        from leetcode.base import Format
        s = Format.formatObj(root)
        print(s)
        return self._maxDepth(root)

    def _maxDepth(self, node):
        if not node:
            return 0
        if not node.children:
            return 1
        return max(self._maxDepth(child) + 1 for child in node.children)

