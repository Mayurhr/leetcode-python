class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        ans=0
        mx=-1
        for num in nums:
            s=str(num)
            max1=int(max(s))
            min1=int(min(s))
            diff=max1-min1
            if diff>mx:
                mx=diff
                ans=num
            elif diff == mx:
                ans+=num
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna