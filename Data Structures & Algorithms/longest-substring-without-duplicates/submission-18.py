class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen_dupe = {}
        # you get this window and make it an input count for each and on the second itearation if one counter is above the sequence count it breaks the loop
        strongest_len = 0
        tmp_len = 0
        start = 0 # consider finding the start point of each
        for x in range(len(s)):
            # you add this chr to the list and if the value is above max counter then you end the len and check which one is the largest with a tmp and checker            
            if not s[x] in last_seen_dupe:
                last_seen_dupe[s[x]] = x
            elif last_seen_dupe[s[x]] < start:
                last_seen_dupe[s[x]] = x
            else:
                strongest_len = max(strongest_len, tmp_len)
                tmp_len -=  last_seen_dupe[s[x]] - start
                start = last_seen_dupe[s[x]] + 1

                last_seen_dupe[s[x]] = x
                continue
            tmp_len += 1

        return max(strongest_len, tmp_len)