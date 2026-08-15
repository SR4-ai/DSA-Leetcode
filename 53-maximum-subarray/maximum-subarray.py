class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        max_sum= float('-inf')
        for i in range(len(nums)):
            curr += nums[i]
            max_sum = max(max_sum,curr)
            if(curr<0):
                curr = 0
        return max_sum