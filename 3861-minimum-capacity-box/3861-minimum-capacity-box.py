class Solution:
    def minimumIndex(self, capacity: List[int], itemSize: int) -> int:
        ans = -1
        for i, x in enumerate(capacity):
            if x >= itemSize and (ans == -1 or x < capacity[ans]):
                ans = i
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna