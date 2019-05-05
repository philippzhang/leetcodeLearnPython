class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic1 = {}
        for i, num in enumerate(nums):
            if num in dic1:
                return [dic1[num], i]
            dic1[target - num] = i
