class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        s1_window = [0] * 26
        tmp_window = [0] * 26

        if n1 > n2:
            return False
        
        for x in range(n1):
            s1_window[ord(s1[x]) - 97] += 1
            tmp_window[ord(s2[x]) - 97] += 1
        
        if s1_window == tmp_window:
                return True

        for x in range(n1, n2):
            tmp_window[ord(s2[x]) - 97] += 1
            tmp_window[ord(s2[x - n1]) - 97] -= 1
            if s1_window == tmp_window:
                return True
        return False
            
        