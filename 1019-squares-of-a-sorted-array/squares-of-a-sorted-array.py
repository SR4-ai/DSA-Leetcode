class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        square_nums = list(map(lambda x:x**2,nums))
        return sorted(square_nums)