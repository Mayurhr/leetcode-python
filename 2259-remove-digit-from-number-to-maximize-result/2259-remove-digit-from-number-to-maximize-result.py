class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        candidates=[]
        for i in range(len(number)):
            if number[i]==digit:
                c=number[:i]+number[i+1:]
                candidates.append(c)
        return max(candidates)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna