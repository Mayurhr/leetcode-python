class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = maximum = 0
        for n in nums:
            count = count + 1 if n == 1 else 0
            maximum = max(maximum, count)
        return maximum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna