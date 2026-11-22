class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element=sum(nums)
        total = sum(int(digit) for num in nums for digit in str(num))
        return abs(total - element)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna