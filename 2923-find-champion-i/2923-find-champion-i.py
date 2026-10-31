class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n=len(grid)
        for i in range(n):
            if sum(grid[i]) == n-1:
                return i
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna