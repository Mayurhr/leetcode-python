class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        winer_streak=0
        winner=arr[0]
        for i in range(1,len(arr)):
            if winner > arr[i]:
                winer_streak += 1
            else:
                winner=arr[i]
                winer_streak = 1
            if winer_streak==k:
                return winner
        return winner

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna