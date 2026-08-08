class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        i=0
        left = i+1
        right = n - 1
        closest = nums[0]+nums[1]+nums[2]

        for i in range(n - 2):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while(left<right):
                total = nums[i]+nums[left]+nums[right]

                if abs(total - target) < abs(closest - target):
                    closest = total



                # Exact match
                if total == target:
                    return total

                elif total < target:
                    left += 1

                else:
                    right -= 1

        return closest
                

                