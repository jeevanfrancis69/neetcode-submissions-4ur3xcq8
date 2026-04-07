class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedString = "".join(c.lower() for c in s if c.isalnum())
        return cleanedString == cleanedString[::-1]