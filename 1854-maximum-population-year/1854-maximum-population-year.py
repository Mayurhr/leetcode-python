class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        count=[0]*101
        for birth,death in logs:
            count[birth-1950]+=1
            count[death-1950]-=1

        population=0
        max_p=0
        answer=101
        for i in range(101):
            population += count[i]

            if population>max_p:
                max_p=population
                answer=1950+i
        return answer