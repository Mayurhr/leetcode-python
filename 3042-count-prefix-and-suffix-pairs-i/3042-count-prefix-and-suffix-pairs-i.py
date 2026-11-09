class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n=len(words)
        count=0
        for i in range(n):
            for j in range(i+1,n):
                s1,s2=words[i] ,words[j]
                if s2.startswith(s1) and s2.endswith(s1):
                    count+=1
        return count 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna