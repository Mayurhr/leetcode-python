class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        left=0
        right=len(s)-1
        while left<right:
            if not s[left].isalpha():
                left+=1
            elif not s[right].isalpha():
                right-=1
            else:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
        return "".join(s)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna