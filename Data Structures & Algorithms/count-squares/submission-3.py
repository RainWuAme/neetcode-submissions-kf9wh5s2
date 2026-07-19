class CountSquares:

    def __init__(self):
        self.countPts = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.countPts[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for px, py in self.pts:
            if abs(x - px) != abs(y - py) or px == x or py == y:
                continue
            res += self.countPts[(x, py)] * self.countPts[(px, y)]

        return res
