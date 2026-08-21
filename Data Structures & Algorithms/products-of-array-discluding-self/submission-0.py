class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_list = [1] * len(nums) #starts on the left
        right_list = [1] * (len(nums) + 1) #starts on the right
        returned_listo = [1] * len(nums)
        for x in range(len(nums) - 1):
            left_list[x] = left_list[x - 1] * nums[x]
            right_list[len(nums) - x - 1] = right_list[len(nums) - x] * nums[len(nums) - x - 1]
        for x in range(len(nums)):
            returned_listo[x] = left_list[x - 1] * right_list[x + 1]
        return returned_listo