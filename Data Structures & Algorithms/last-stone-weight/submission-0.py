class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # x == y , both destroyed
        # x < y, x destroyed. y = y-x
        
        while len(stones) > 1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur:
                stones.append(cur)
        return stones[0] if stones else 0