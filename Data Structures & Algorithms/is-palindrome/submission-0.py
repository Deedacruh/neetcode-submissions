class Solution:
    def isPalindrome(self, s: str) -> bool:
        test_dummy = ""
        length = len(s)
        for x in range(length):
            num = ord(s[x])
            if (num >= 97 and num <= 122) or (num >= 48 and num <= 57):
                test_dummy += s[x]
            elif (num >= 65 and num <= 90):
                test_dummy += chr(num + 32)
        length_dummy = len(test_dummy)
        for x in range(int(length_dummy / 2) + (length_dummy % 2)):
            if test_dummy[x] != test_dummy[length_dummy - 1 - x]:
                return False
        return True