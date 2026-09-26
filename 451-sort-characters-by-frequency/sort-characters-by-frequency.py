class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        
        # Sort characters by frequency in descending order
        sorted_chars = sorted(s, key=lambda x: (-count[x], x))
        
        # Join and return the sorted result
        return "".join(sorted_chars)