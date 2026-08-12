class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        r = 0
        n = len(nums)

        curr_sum = 0
        min_size = float('inf')

        while r < n:

            # Expand window
            curr_sum += nums[r]

            # Shrink window
            while curr_sum >= target:

                min_size = min(min_size, r - l + 1)

                curr_sum -= nums[l]
                l += 1

            r += 1

        if min_size == float('inf'):
            return 0

        return min_size


'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        res = float("inf")

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                res = min(r - l + 1, res)

                total -= nums[l]
                l += 1

        return 0 if res == float("inf") else res
'''
