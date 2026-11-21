class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n=len(s)
        c=s.count(letter)
        return (c*100) // n


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna