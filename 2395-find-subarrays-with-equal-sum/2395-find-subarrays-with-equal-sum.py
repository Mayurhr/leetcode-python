class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        seen=set()
        for i in range(len(nums)-1):
            csum=nums[i]+nums[i+1]
            if csum in seen:
                return True
            seen.add(csum)
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna