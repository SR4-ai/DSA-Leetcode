class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        first = -1
        last = -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        return [first, last]
        '''
        def find_first():
            low = 0
            high = len(nums) - 1
            answer = -1

            while low <= high:

                mid = (low + high) // 2

                if nums[mid] == target:
                    answer = mid
                    high = mid - 1

                elif nums[mid] < target:
                    low = mid + 1

                else:
                    high = mid - 1

            return answer

        def find_last():
            low = 0
            high = len(nums) - 1
            answer = -1

            while low <= high:

                mid = (low + high) // 2

                if nums[mid] == target:
                    answer = mid
                    low = mid + 1

                elif nums[mid] < target:
                    low = mid + 1

                else:
                    high = mid - 1

            return answer

        first = find_first()
        last = find_last()

        return [first, last]