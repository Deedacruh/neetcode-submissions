class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left_pointer = 0
         # these two babies are going to start at the same place and move left and right accordingly
        res = 0
        strongest_candidate = 0
        max_char = 0
        current_chars = [0] * 26
        for right_pointer in range(len(s)):
            current_chars[ord(s[right_pointer]) - 65] += 1
            max_char = max(max_char, current_chars[ord(s[right_pointer]) - 65])
            while (right_pointer - left_pointer + 1) - max_char > k:
                current_chars[ord(s[left_pointer]) - 65] -= 1
                left_pointer += 1
            res = max(res, right_pointer - left_pointer + 1)
        return res