class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0
        for i in range(len(s)):
            freq = {}
            for j in range(i,len(s)):
                ch = s[j]

                if ch in freq:
                    freq[ch] += 1
                else:
                    freq[ch] = 1

                ### OUTput LIMIT reached if we use print statement here(logic is correct)

                # print(s[i:j+1], freq)

                max_freq = max(freq.values())
                min_freq = min(freq.values())

                beauty = max_freq - min_freq

                answer += beauty
        return answer



