class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_kept=left=0
        for i in range(len(nums)):
            while nums[i] > nums[left] * k:
                left+=1
            max_kept=max(max_kept , i - left +1)
        return len(nums) - max_kept

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna