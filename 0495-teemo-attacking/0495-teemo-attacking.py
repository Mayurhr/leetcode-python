class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        if not timeSeries:
            return 0
        total_time=0
        for i in range(len(timeSeries)-1):
            gap=timeSeries[i+1]-timeSeries[i]
            total_time+=min(duration, gap)
        total_time+=duration
        return total_time

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna