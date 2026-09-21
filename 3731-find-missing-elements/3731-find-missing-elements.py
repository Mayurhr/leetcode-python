class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minval=min(nums)
        maxval=max(nums)
        numsset=set(nums)

        return [x for x in range(minval,maxval+1) if x not in numsset]