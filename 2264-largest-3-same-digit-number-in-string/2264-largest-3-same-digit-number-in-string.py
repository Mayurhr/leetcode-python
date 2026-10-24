class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            sub = str(i) * 3
            if sub in num:
                return sub
        return ""

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna