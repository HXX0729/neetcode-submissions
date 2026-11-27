class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalphanumeric(a):
            if ord("A") <= ord(a) <= ord("Z") or ord("a") <= ord(a) <= ord("z") or ord("0") <= ord(a) <= ord("9"):
                return True
            else:
                return False

        l, r = 0, len(s)-1
        while l < r:
            while l < r and not isalphanumeric(s[l]):
                l += 1
            while l < r and not isalphanumeric(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():

                return False
            l += 1
            r -= 1
        return True