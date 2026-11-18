class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        result=[]
        for ch in set(words[0]):
            count=min(word.count(ch) for word in words)
            result += [ch]*count
        return result


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna