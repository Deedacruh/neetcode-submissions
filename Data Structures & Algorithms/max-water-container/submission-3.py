class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''create two pointers that start at the beginning and end, they move + 1 
        for the first pointer and -1 for the last and the'''
        tmp_container = 0
        largest_container = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            tmp_container = min(heights[l], heights[r]) * (r - l)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1 # make a case to see if these two equal and compare the adjustments by 1
            largest_container = max(tmp_container, largest_container)
        return largest_container