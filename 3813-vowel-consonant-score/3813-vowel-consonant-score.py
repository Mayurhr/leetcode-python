
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels=consonants=0
        for ch in s:
            if ch in "aeiou":
                vowels += 1
            elif ch.isalpha():
                consonants += 1
        if consonants == 0:
            return 0
        return vowels // consonants


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna