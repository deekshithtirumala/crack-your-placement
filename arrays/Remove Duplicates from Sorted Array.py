class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0

        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[index], nums[i] = nums[i], nums[index]
                index+=1
        nums[index] = nums[-1]
        return index+1
        
