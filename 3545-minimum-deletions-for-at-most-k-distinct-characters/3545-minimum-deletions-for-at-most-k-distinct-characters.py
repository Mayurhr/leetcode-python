class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freq=sorted(Counter(s).values())
        if len(freq) <= k:
            return 0
        return sum(freq[:len(freq)-k])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna