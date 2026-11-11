
class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            mini = nums[i]
            maxi = nums[i]
            for j in range(i,len(nums)):
                mini = min(mini, nums[j])
                maxi = max(maxi, nums[j])
                count += maxi - mini
        return count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna