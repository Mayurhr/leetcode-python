class Solution:
    def minMoves(self, nums: List[int]) -> int:
        l=len(nums)
        mx=max(nums)
        s=sum(nums)
        return mx*l-s