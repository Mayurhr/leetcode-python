class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row=[1]
        for i in range(1,rowIndex+1):
            nextVal=row[-1]*(rowIndex-i+1)//i
            row.append(nextVal)
        return row

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna