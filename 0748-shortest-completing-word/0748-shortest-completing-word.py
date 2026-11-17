class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        letters = ""
        for ch in licensePlate:
            if ch.isalpha():
                letters += ch.lower()
        ans = ""
        for word in words:
            temp = word.lower()
            for ch in letters:
                if ch in temp:
                    temp = temp.replace(ch, "", 1)
                else:
                    break
            else:
                if ans == "" or len(word) < len(ans):
                    ans = word
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna