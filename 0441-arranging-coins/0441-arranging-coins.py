class Solution:
    def arrangeCoins(self, n: int) -> int:
        row=0
        while n >= row +1:
            row += 1
            n -= row
        return row

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna