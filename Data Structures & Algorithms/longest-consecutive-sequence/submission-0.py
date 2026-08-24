class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        standard_dictionary = set()
        tmp_sequence_count = 0 #this changes and compares each sequence length
        for x in range(len(nums)):
            standard_dictionary.add(nums[x])
        x = False
        tmp_count = 0
        n = 0
        strongest = 0
        while n <= (len(nums) - 1):
            tmp_var = nums[n]
            tmp_count = 0
            while x == False:
                if tmp_var in standard_dictionary:
                    tmp_var -= 1
                else:
                    x = True
                    tmp_var += 1
            while x == True:
                if tmp_var in standard_dictionary:
                    standard_dictionary.remove(tmp_var)
                    tmp_count += 1
                    tmp_var += 1
                else:
                    x = False
            n += 1
            if strongest < tmp_count:
                strongest = tmp_count
        return strongest


                