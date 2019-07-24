class Iterator(object):
    def __init__(self, nums):
        """
         Initializes an iterator object to the beginning of a list.
         :type nums: List[int]
         """
        self.nums = nums
        self.i = 0

    def hasNext(self):
        """
         Returns true if the iteration has more elements.
         :rtype: bool
         """
        return self.i < len(self.nums)

    def next(self):
        """
         Returns the next element in the iteration.
         :rtype: int
         """
        v = self.nums[self.i]
        self.i += 1
        return v
