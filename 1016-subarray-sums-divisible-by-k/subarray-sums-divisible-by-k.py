class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {0: 1}
        prefix = 0
        ans = 0

        for num in nums:
            prefix += num

            remainder = prefix % k

            ans += count.get(remainder, 0)

            count[remainder] = count.get(remainder, 0) + 1

        return ans