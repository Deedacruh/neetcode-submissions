class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ans = {}
        output = []
        for x in range(len(nums)):
            dict_ans.setdefault(nums[x], 0)
            dict_ans[nums[x]] += 1

        sorted_dict = dict(
            sorted(dict_ans.items(), key=lambda item: item[1], reverse=True)
        )
        keys = list(sorted_dict.keys())
        return keys[0:k]