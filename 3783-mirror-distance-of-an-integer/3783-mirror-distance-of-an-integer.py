class Solution(object):
    def mirrorDistance(self, n):
        m=int(str(n)[::-1])
        return abs(n-m)
        