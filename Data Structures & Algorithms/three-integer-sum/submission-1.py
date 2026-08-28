class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final_ans = []
        for index, select in enumerate(nums):
            if index > 0 and select == nums[index - 1]:
                continue
            l, r = index + 1, len(nums) - 1
            while l < r:
                if select > -1 * (nums[l] + nums[r]):
                    r -= 1
                elif select < -1 * (nums[l] + nums[r]):
                    l += 1
                else:
                    final_ans.append([select, nums[l], nums[r]])
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
        return final_ans