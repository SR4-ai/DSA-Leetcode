class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        k = len(s)
        
        for i in range(k):
            if s[i:]+s[:i] == goal:
                return True
        
        return False
        