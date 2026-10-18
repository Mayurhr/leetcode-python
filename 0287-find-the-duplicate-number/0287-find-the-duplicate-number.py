class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        m=len(nums)
        nums.sort()
        for i in range(m-1):
            if nums[i]==nums[i+1]:
                return nums[i]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna