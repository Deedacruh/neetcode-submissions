class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorting_dict = {}
        returned_list = []
        for x in strs:
            ascii_table = [0] * 26
            for y in x:
                ascii_table[ord(y) - 97] += 1
            sorting_dict.setdefault(tuple(ascii_table), []).append(x)
        for x in sorting_dict.keys():
            returned_list.append(sorting_dict[x])
        return returned_list