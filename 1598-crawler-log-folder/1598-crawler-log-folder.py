class Solution:
    def minOperations(self, logs: list[str]) -> int:
        depth=0
        for log in logs:
            if log == "../":
                depth=max(0 , depth-1)
            elif log == "./":
                continue
            else:
                depth+=1
        return depth 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna