class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        total =0
        for i in range(n):
            if i%2==0:
                total+=nums[i]
            else:
                total-=nums[i]
        return total

