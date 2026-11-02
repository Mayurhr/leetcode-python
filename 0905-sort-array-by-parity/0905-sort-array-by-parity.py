class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        ans1=[]
        ans2=[]
        for num in nums:
            if num % 2==0:
                ans1.append(num)
            else:
                ans2.append(num)
        return ans1+ans2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna