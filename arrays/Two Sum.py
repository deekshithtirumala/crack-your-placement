class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if nums[i] in dic:
                return [i, dic[nums[i]]]
            else:
                dic[x] = i
