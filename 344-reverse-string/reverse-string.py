class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        n = len(s)
        left = i
        right = n-1
        while left<=right:
            s[left],s[right] = s[right],s[left]
            left+=1
            right-=1
