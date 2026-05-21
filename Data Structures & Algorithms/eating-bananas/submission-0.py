class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 找到第一个 k where sum(each pile in piles/k) <= h

        def can_finish(k):
            s = 0
            for p in piles:
                s += (p + k - 1) // k
            return s <= h
        
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) //2
            if can_finish(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

