class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def searchindex(nums,low,high):
            if low>high:
                return -1
            mid = (low+high)//2
            if target == nums[mid]:
                return mid
            elif target<nums[mid]:
                return searchindex(nums,low,mid-1)
            else:
                return searchindex(nums,mid+1,high)

        return searchindex(nums, 0, len(nums) - 1)