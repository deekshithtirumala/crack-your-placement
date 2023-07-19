class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countZeors = 0

        indics = []
        zeroOccur = False
        for i in range(len(nums)):
            if nums[i]==0:
                indics.append(i)
                zeroOccur = True
            else:
                if zeroOccur:
                    nums[indics[0]], nums[i] = nums[i], nums[indics[0]]
                    indics = indics[1:]
                    indics.append(i)

        
