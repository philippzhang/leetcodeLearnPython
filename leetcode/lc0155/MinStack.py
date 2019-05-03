from leetcode.base.structure.ListNode import ListNode


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.tail = ListNode(None)
        self.mintail = ListNode(None)
        self.length = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        tmp = ListNode(x)
        tmp.before = self.tail
        self.tail.next = tmp
        self.tail = self.tail.next

        if self.mintail.val is None or x < self.mintail.val:
            tmp = ListNode(x)
            tmp.before = self.mintail
            self.mintail.next = tmp
            self.mintail = self.mintail.next
        else:
            tmp = ListNode(self.mintail.val)
            tmp.before = self.mintail
            self.mintail.next = tmp
            self.mintail = self.mintail.next

    def pop(self):
        """
        :rtype: None
        """
        tmp = self.tail
        self.tail = tmp.before
        tmp.before = None
        self.tail.next = None
        self.length -= 1

        tmp = self.mintail
        self.mintail = tmp.before
        tmp.before = None
        self.mintail.next = None

    def top(self):
        """
        :rtype: int
        """
        return self.tail.val

    def getMin(self):
        """
        :rtype: int
        """
        return self.mintail.val