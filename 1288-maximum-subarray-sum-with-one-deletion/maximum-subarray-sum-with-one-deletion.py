class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        no_delete = arr[0] 
        one_delete = float('-inf') 
        ans = arr[0] 
        for i in range(1, len(arr)): 
            one_delete = max(one_delete + arr[i], no_delete) 
            no_delete = max(arr[i], no_delete + arr[i]) 
            ans = max(ans, no_delete, one_delete) 
        return ans