class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float('inf')        
        for i in range(n):
            curr_sum = 0
            for j in range(i, min(n, i + r)):
                curr_sum += nums[j]
                if j - i + 1 >= l and curr_sum > 0:
                    ans = min(ans, curr_sum)     
        return ans if ans != float('inf') else -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna