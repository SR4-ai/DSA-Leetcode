class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''max_product = float('-inf')
        curr = 1
        for i in range(len(nums)):
            curr *= nums[i]
            max_product = max(max_product,curr)
            if curr==0:
                curr = 1
        return max_product
        '''
        prefix = 1
        suffix = 1
        max_prod= float('-inf')
        n = len(nums)
        for i in range (n):
            if(prefix == 0):
                prefix = 1
            elif(suffix==0):
                suffix = 1
            prefix *= nums[i] 
            suffix *= nums[n-i-1] 
            max_prod = max(max_prod,max(prefix,suffix))
        return max_prod

