class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''
        for ch in s:
            if ch.isalnum():
                new_string += ch.lower()
        if new_string == new_string[::-1]:
            return True
        return False
