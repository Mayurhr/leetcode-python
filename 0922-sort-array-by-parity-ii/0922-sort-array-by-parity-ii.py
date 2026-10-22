class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        e, o = 0, 1
        while e < len(nums):
            if nums[e] % 2:
                nums[e], nums[o] = nums[o], nums[e]
                o += 2
            else:
                e += 2
        return nums

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna