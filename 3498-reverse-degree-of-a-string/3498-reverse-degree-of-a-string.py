class Solution:
    def reverseDegree(self, s: str) -> int:
        m=0
        for i in range(len(s)):
            m+=(26-(ord(s[i])-ord('a')))*(i+1)
        return m