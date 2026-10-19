class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for detail in details:
            if int(detail[11:13])>60:
               count+=1
            else:
                count+=0
        return count  

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna