class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            if num % 2==0:
                res.append(0)
            else:
                res.append(1)
        res.sort()
        return res