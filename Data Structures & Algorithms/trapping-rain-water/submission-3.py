class Solution:
    def trap(self, height: List[int]) -> int:
        # water area = min (max(R), max(L)) - height[i]
        n = len(height)
        maxR, maxL = [0] * n, [0] * n
        for i in range(1, n):
            maxL[i] = max(maxL[i - 1], height[i - 1])
        for i in range(n-2,-1,-1):
            maxR[i] = max(maxR[i + 1], height[i + 1])
        res = 0
        for i in range(n):
            temp = min(maxR[i], maxL[i]) - height[i]
            if temp > 0:
                res += temp
        return res

# height=[4,2,0,3,2,5]
# n = 6
# maxL = [0,4,4,4,4,4]
# maxR = [        ,5,0]