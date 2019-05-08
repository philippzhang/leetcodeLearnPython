class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.tree = []
        self.inOrder(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.tree:
            return self.tree.pop(0)
        else:
            return None

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.tree:
            return True
        else:
            return False

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.tree.append(root.val)
        self.inOrder(root.right)
        return