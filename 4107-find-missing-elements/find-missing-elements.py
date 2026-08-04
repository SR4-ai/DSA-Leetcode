class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)

        smallest = min(nums)
        largest = max(nums)

        ans = []

        for x in range(smallest, largest + 1):
            if x not in s:
                ans.append(x)

        return ans



    ''' nums = sorted(nums)
        last = nums[-1]
        first = nums[0]
        if first==1:
            total = (last*(last+1))/2
        if first == 2:
            total = (last*(last+1))/2 -1
        total = (last*(last+1))/2 - ((first-1)*(first))/2

        total_nums = sum(nums)

        remaining = total - total_nums
        if remaining == 0:
            return []

        else:
            i = first + 1
            for i in range(remaining+1):
                nums.append(i)
                remaining = remaining-i
            return sorted(nums)'''

        