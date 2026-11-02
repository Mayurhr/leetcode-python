class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n=len(nums)
        return max(abs(nums[i] - nums[ (i+1)%n ]) for i in range(n))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna