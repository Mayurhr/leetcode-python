class Solution:
    from collections import Counter
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts=Counter(arr)
        return len(set(counts.values()))==len(counts)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna