class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        if len(s) != len(t):
            return False
        for x in range(len(s)):
            for y in range(26):
                if chr(97 + y) == s[x]:
                    dict_s[s[x]] = dict_s.get(s[x], 0) + 1
                if chr(97 + y) == t[x]:
                    dict_t[t[x]] = dict_t.get(t[x], 0) + 1
        for z in range(26):
            if dict_t.get(chr(97 + z), 0) != dict_s.get(chr(97 + z), 0):
                return False
        return True
