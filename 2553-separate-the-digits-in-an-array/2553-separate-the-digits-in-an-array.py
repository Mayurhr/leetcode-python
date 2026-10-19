class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        result=[]
        for num in nums:
            for digit in str(num):
                result.append(int(digit))
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna