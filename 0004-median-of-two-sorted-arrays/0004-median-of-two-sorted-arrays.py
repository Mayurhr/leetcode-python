class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s=sorted(nums1+nums2); return (s[len(s)//2]+s[~len(s)//2])/2