class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {0:-1}
        ans = count = 0
        for i ,x in enumerate(nums):
            count += 1 if x==1 else -1
            if count in freq:
                ans = max(ans,i-freq[count])
            else:
                freq[count] = i
        return ans