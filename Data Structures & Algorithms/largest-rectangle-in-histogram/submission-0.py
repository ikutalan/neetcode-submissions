class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 暴力解法
        res = 0
        for i, h in enumerate(heights):
            # 分别找i两边最小的柱子
            l = i
            while l > 0 and heights[l - 1] >= h:
                l -= 1
            r = i
            while r < len(heights) - 1 and heights[r+1] >= h:
                r += 1
            res = max(res, (r-l+1)*h) 
        return res
