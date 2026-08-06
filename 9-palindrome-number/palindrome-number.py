class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_rev = ''.join(reversed(str(x)))
        if(x_rev==str(x)):
            return True
        else:
            return False