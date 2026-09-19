class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # make a tmp dict and and a non tmp one for this s1
        # Ok because these two only contain lowercase letters, that means that. we can use a 26 count list
        letter_count = [0] * 26
        new_guy = False
        # WE COULD ALSO MAKE 2 DICTIONARIES AND JUST COMPARE EACH ELEMENT TO EACH IN BIG O OF 1
        first_seen_holder = [0] * 26
        for x in range(len(s1)):
            letter_count[ord(s1[x]) - 97] += 1
        tmp_count = [0] * 26
        for x in range(len(s2)):
            index = ord(s2[x]) - 97
            if letter_count[index] > 0: # means that that letter does exist
                tmp_count[index] += 1
                if tmp_count[index] == 1:
                    # Beginming or first occurence.
                    first_seen_holder[index] = tmp_count.copy()
                if tmp_count[index] > letter_count[index]:
                    for z in range(26):
                        tmp_count[z] -= first_seen_holder[index][z]
                    first_seen_holder[index] = tmp_count.copy()
# We get the charcater where the problem happened, what's that letter?
                """Main thing we need to do is salvage to remove or just straight up remove the data added before the first appearance of that redundancy"""
                if tmp_count == letter_count:
                    return True
            else:
                # this where this messes up of course so we must adapt this
                tmp_count = [0] * 26
        return False