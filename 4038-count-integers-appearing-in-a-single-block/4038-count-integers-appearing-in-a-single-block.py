class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        seen=set()
        repeat=set()
        for i in range(len(nums)):
            if nums[i] in seen and nums[i] != nums[i-1]:
                repeat.add(nums[i])
            seen.add(nums[i])
        return len(seen) - len(repeat)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna