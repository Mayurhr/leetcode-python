class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result=""
        for char in order:
            result+=char*s.count(char)
        for char in s:
            if char not in order:
                result+=char
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna