class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        return self._maxDepth(root)

    def _maxDepth(self, node):
        if not node:
            return 0
        if not node.children:
            return 1
        return max(self._maxDepth(child) + 1 for child in node.children)

