class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.val = self.iter.next()
        self.hasnext = True

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.val

    def next(self):
        """
        :rtype: int
        """
        ans = self.val
        if self.iter.hasNext():
            self.val = self.iter.next()
        else:
            self.hasnext = False
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.hasnext
