class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        res = [[]]
        for i in range(n):
            if nums[i] != nums[i - 1] or i == 0:
                cur = [x + [nums[i]] for x in res]
            else:
                # 使用cur列表记录上一次新创建的子集
                cur = [x + [nums[i]] for x in cur]
            res += cur
        return res
