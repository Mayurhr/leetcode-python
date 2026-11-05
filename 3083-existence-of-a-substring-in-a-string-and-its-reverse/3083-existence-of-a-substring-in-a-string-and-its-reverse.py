class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reversed_s=s[::-1]
        return any(s[i:i+2] in reversed_s for i in range(len(s)-1))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna