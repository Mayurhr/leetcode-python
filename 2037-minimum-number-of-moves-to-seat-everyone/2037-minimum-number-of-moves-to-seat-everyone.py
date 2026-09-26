class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        return sum(abs(seats-students) for seats,students in zip(seats,students))