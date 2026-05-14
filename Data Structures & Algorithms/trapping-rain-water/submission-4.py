class Solution:
    def trap(self, height: List[int]) -> int:
        # water area = min (max(R), max(L)) - height[i]
        # MaxR and MaxL 包含自己
        n = len(height)
        maxR, maxL = [0] * n, [0] * n
        maxL[0] = height[0]
        for i in range(1, n):
            maxL[i] = max(maxL[i - 1], height[i])
        
        maxR[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            maxR[i] = max(maxR[i + 1], height[i])
        
        res = 0
        for i in range(n):
            res += min(maxR[i], maxL[i]) - height[i]
        return res