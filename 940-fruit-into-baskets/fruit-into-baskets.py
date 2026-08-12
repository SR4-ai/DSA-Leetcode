class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        l = 0
        freq = {}
        n = len(fruits)
        max_len = -1
        for r in range(len(fruits)):
            freq[fruits[r]] = freq.get(fruits[r],0)+1     


            while(len(freq)>2):
                freq[fruits[l]] -= 1
                if(freq[fruits[l]]==0):
                    del freq[fruits[l]]

                l+=1
            if len(freq) <= 2:
                max_len = max(max_len, r - l + 1)

        return max_len