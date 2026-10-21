class Solution:
    def replaceDigits(self, s: str) -> str:
        return "".join(s[i] if i % 2 == 0 else chr(ord(s[i - 1]) + int(s[i])) for i in range(len(s)))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna