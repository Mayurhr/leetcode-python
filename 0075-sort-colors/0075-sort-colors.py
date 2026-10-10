class Solution:
    def sortColors(self, nums: list[int]) -> None:
        count_0=nums.count(0)
        count_1=nums.count(1)
        count_2=nums.count(2)
        index=0
        for _ in range(count_0):
            nums[index]=0
            index+=1
        
        for _ in range(count_1):
            nums[index]=1
            index+=1
        
        for _ in range(count_2):
            nums[index]=2
            index+=1