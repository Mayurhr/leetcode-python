class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        similar=set(nums1).intersection(nums2)
        return list(similar)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna