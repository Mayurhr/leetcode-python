class Solution:
    def reformatNumber(self, number: str) -> str:
        s = ""
        for ch in number:
            if ch.isdigit():
                s += ch
        ans = ""
        while len(s) > 4:
            ans += s[:3] + "-"
            s = s[3:]
        if len(s) == 4:
            ans += s[:2] + "-" + s[2:]
        else:
            ans += s
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna