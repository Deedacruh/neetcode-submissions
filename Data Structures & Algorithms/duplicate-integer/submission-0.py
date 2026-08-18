class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for x in range(len(nums)):
            if not (nums[x] in hash):
                hash[nums[x]] = 1
            else:
                return True
        return False