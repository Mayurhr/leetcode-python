class Solution:
    def maxDifference(self, s: str) -> int:
        counts=Counter(s)
        max_odd=0
        min_even=float('inf')
        for freq in counts.values():
            if freq % 2 == 1:
                max_odd=max(max_odd , freq)
            else:
                min_even=min(min_even , freq)
        return max_odd - min_even

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna