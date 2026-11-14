class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans=[]
        for n in nums:
            if ans and ans[-1][-1]+1 == n:
                ans[-1][-1] = n
            else:
                ans.append([n, n])
        return [f"{a}->{b}" if a != b else f"{a}" for a,b in ans]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna