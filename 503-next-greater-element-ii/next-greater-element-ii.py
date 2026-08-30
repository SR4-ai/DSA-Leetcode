class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums = nums * 2
        result = []

        for i in range(n):
            found = False

            for j in range(i + 1, i + n):
                if nums[j] > nums[i]:
                    result.append(nums[j])
                    found = True
                    break

            if not found:
                result.append(-1)

        return result