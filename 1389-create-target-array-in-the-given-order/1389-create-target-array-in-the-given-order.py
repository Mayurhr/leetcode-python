class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        target=[]
        for i in range(len(nums)):
            target.insert(index[i],nums[i])
        return target

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna