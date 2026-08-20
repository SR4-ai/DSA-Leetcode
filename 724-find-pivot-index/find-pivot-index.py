class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''n = len(nums)
        suffix = [0] * n
        prefix = [0] * n

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i + 1]
        for i in range(1,n):
            prefix[i] = prefix[i-1]+nums[i-1]
        for i in range(n):
            if(prefix[i]==suffix[i]):
                return i
        return -1
        '''
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            
            right = total - nums[i] - left
            if(left == right):
                return i
            left += nums[i]
        return -1
