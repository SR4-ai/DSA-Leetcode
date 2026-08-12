class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        freq = {}
        
        max_len = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0)+1     


            while(freq[s[r]]>1):
                freq[s[l]] -= 1
                if(freq[s[l]]==0):
                    del freq[s[l]]

                l+=1
            
            max_len = max(max_len, r - l + 1)

        return max_len