class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s>9*n:
            return -1
        result=""
        for i in range(n):
            digit=min(s,9)
            result += str(digit)
            s -= digit
        return int(result)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna