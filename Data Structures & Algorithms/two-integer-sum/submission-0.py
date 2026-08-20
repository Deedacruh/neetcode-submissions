class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_num = {}
        for x in range(len(nums)):
            if not target - nums[x] in index_num:
                index_num[nums[x]] = x
            else:
                return [index_num[target - nums[x]], x]
