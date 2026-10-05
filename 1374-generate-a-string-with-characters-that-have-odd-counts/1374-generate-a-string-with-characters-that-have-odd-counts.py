class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 != 0:
            return n*'a'
        else:
            return ('a'*(n-1)+'b')