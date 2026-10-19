class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        min1 = min2 = float('inf')
        for p in prices:
            if p < min1:
                min2 = min1
                min1 = p
            elif p < min2:
                min2 = p
        total_cost= min1 + min2
        return money - total_cost if total_cost <= money else money


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna