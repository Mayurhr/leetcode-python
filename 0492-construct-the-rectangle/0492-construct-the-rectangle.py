from math import sqrt
class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        w=int(sqrt(area))
        while area % w !=0:
            w-=1
        return [area//w,w]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna