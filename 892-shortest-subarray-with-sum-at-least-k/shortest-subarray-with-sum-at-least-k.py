class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        dq = deque()
        ans = float('inf')

        for i in range(n + 1):

            while dq and prefix[i] - prefix[dq[0]] >= k:
                ans = min(ans, i - dq.popleft())

            while dq and prefix[dq[-1]] >= prefix[i]:
                dq.pop()

            dq.append(i)

        return -1 if ans == float('inf') else ans