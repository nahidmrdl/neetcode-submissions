class Solution:
    def isPalindrome(self, s: str) -> bool:
        return "".join(c for c in s.lower().replace(" ", "") if c.isalnum()) == "".join(c for c in s.lower().replace(" ", "") if c.isalnum())[::-1]
        