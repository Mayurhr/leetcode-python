class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq = Counter(str(n))
        score = 0
        for d, count in freq.items():
            score += int(d) * count   
        return score