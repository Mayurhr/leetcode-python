class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        total=0
        for i in range(len(nums)):
            if i- k >=0 and nums[i] <= nums[i-k]:
                continue
            if i + k < len(nums) and nums[i] <= nums[i+k]:
                continue
            total+=nums[i]
        return total

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna