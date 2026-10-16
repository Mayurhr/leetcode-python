
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total = 0
        product = 1
        while n > 0:
            digit = n % 10
            total += digit
            product *= digit
            n //= 10
        return product - total

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna