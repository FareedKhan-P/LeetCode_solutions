class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join([char for char in s.lower() if "a" <= char <= "z" or "0" <= char <= "9"])
        return string[::-1] == string