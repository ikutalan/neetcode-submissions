class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)  
        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            res = x - y
            if res:
                heapq.heappush(max_heap, -res)
        return -max_heap[0] if max_heap else 0