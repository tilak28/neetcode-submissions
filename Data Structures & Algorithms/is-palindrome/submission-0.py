class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = list(filter(str.isalpha, s.lower()))

        i = 0
        j = len(chars) - 1

        while i < j:
            if chars[i] != chars[j]:
                return False
            i += 1
            j -= 1

            while chars[i] == chars[j] and i == j:
                return True