class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in range(len(s)):
            if s[x] in {"(", "{", "["}:
                stack.append(s[x])
            elif s[x] in {"}", "]", ")"}:
                if len(stack) == 0:
                    return False
                elif s[x] in {chr(ord(stack[-1]) + 2), chr(ord(stack[-1]) + 1)}:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True