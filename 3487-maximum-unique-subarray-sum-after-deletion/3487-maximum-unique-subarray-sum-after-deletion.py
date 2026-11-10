class Solution:
    def maxSum(self, nums: List[int]) -> int:
        arr=set(nums)
        positive=[x for x in arr if x > 0]
        if positive:
            return sum(positive)
        return max(nums)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna