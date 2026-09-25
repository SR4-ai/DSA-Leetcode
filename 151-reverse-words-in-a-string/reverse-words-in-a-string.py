class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        words = s.split()
        n = len(words)
        low = 0
        high = n-1
        while(low<=high):
            words[low],words[high] = words[high],words[low]
            low+=1
            high-=1
        return " ".join(words)