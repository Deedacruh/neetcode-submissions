class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for x in range(len(strs)):
            encoded_string += str(len(strs[x])) + "#" + strs[x]
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        temp_counter = 0
        x = 0
        tmp_len = ""
        while x <= -1 + len(s):
            temp_item = ""
            if s[x] == "#":
                x +=1
                # when triggered turn this string that has the full len of the digits and turns
                #into an integer
                tmp_len = int(tmp_len)
                for y in range(tmp_len):
                    temp_item += s[x]
                    x += 1
                decoded_strs.append(temp_item)
                tmp_len = ""
                continue
            tmp_len += s[x]
            x += 1
        return decoded_strs
            