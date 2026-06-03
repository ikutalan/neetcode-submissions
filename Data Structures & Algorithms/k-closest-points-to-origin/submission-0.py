class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            dist = p[0] * p[0] + p[1] * p[1]
            heapq.heappush(heap, (-dist, p))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [p for _, p in heap]