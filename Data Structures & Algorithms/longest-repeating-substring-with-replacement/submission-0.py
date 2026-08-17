class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charIndex = {}
        output = 0
        max_freq = 0

        for r in range(len(s)):
            charIndex[s[r]] = charIndex.get(s[r] , 0) + 1
            max_freq = max(max_freq , charIndex[s[r]])

            windowSize = r + 1 - l

            if windowSize - max_freq > k:
                charIndex[s[l]] -= 1
                l += 1
            
            output = max(output, r + 1 - l)
        
        return output
