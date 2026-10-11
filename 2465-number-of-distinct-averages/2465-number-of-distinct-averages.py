class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort()
        seen = set()
        i = 0
        j = len(nums) - 1
        while i < j:
            seen.add(nums[i] + nums[j])
            i += 1
            j -= 1
        return len(seen)