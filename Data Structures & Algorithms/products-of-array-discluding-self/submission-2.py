class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_list = [1] * len(nums)
        right_list = [1] * len(nums)
        outputted_list = []
        for x in range(len(nums)):
            if x == 0:
                left_list[x] = nums[x]
                right_list[len(nums) - x - 1] = nums[len(nums) - x - 1]
            else:
                left_list[x] = nums[x] * left_list[x - 1]
                right_list[len(nums) - x - 1] = right_list[len(nums) - x] * nums[len(nums) - x - 1]
        for x in range(len(nums)):
            if (x == 0):
                outputted_list.append(right_list[x + 1])
            elif (x == (len(nums) - 1)):
                outputted_list.append(left_list[x + - 1])
            else:
                outputted_list.append(left_list[x + - 1] * right_list[x + 1])
        return outputted_list