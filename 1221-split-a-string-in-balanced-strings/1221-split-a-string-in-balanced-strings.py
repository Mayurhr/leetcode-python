class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bcount=0
        b=0
        for char in s:
            if char == 'L':
                b+=1
            else:
                b-=1
            if b==0:
                bcount+=1
        return bcount