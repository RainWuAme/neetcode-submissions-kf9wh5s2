class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            stone1 = -heapq.heappop(maxHeap)
            stone2 = -heapq.heappop(maxHeap)
            smashed_stone = stone1 - stone2
            if smashed_stone > 0:
                heapq.heappush(maxHeap, -smashed_stone)

        return -maxHeap[0] if len(maxHeap) > 0 else 0