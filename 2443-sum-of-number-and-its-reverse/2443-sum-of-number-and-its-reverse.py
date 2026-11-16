class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for x in range(num+1):
            rev_x=int(str(x)[::-1])
            if x + rev_x == num:
                return True
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna