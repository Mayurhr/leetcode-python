class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowles="aeiou"
        vowels_count={}
        consts_count={}
        for char in s:
            if char in vowles:
                vowels_count[char]=vowels_count.get(char,0)+1
            else:
                consts_count[char]=consts_count.get(char, 0)+1

        vmax=max(vowels_count.values(),default=0)
        cmax=max(consts_count.values(),default=0)
        return vmax+cmax