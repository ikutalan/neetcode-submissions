class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers
        # r, l, move to center
        # water = short bond - height[i]
        n = len(height)
        res = 0
        l = 0
        r = n - 1
        maxL = height[l]
        maxR = height[r]
        while l < r:
            if maxL > maxR:
                r -= 1
                maxR = max(height[r], maxR)
                res += maxR - height[r]
            else:
                l += 1
                maxL = max(height[l],maxL)
                res += maxL - height[l]
        return res