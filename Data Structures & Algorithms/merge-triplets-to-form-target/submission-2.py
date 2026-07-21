class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = [0, 0, 0]
        for i, t in enumerate(triplets):
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            if t[0] == target[0]:
                good[0] = 1
            if t[1] == target[1]:
                good[1] = 1
            if t[2] == target[2]:
                good[2] = 1

        return sum(good) == 3
