class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.replace("-","").upper()
        s=s[::-1]
        result=[]
        for i in range(len(s)):
            if i>0 and i%k==0:
                result.append("-")
            result.append(s[i])
        return "".join(result)[::-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna