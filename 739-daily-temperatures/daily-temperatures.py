class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        '''result = []
        n = len(temperatures)
        
        for i in range(n):
            found = False
            for j in range (i+1,n):
                if temperatures[j]>temperatures[i]:
                    result.append(j-i)
                    found = True
                    break
                
            if not found:
                result.append(0)
            
        return result
        '''
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev

            stack.append(i)

        return result


