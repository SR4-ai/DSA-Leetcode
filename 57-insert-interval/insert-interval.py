class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        intervals.append(newInterval)
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start,end in intervals[1:]:
            lastend = output[-1][1]
            if(start<=lastend):
                output[-1][1] = max(lastend,end)
            else:
                output.append([start,end])
        return output