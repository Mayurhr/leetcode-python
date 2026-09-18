class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        A=abs(x-z)
        B=abs(y-z)
        if A<B:
            return 1
        elif B<A:
            return 2
        else:
            return 0