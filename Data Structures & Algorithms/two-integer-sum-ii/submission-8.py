class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer_left = 0
        pointer_right = len(numbers) - 1
        loop_check = False
        while True:
            if numbers[pointer_left] + numbers[pointer_right] > target:
                pointer_right -= 1
            elif numbers[pointer_left] + numbers[pointer_right] < target:
                pointer_left += 1
            elif numbers[pointer_left] + numbers[pointer_right] == target:
                return [pointer_left + 1, pointer_right + 1]