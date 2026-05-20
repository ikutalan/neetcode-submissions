class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonic stack
        res = 0
        stack = []
        n = len(heights)
        for i in range(n):
            h = 0
            while stack and heights[i] < heights[stack[-1]]:
                j = stack.pop()
                h = heights[j]
                # [i] is the first right element shorter than [j]
                # what's current in the stack top is the first 
                # left element shorter than [j]
                r = i
                l = stack[-1] if stack else -1
                res = max(res, h * (r - l -1))
            stack.append(i)
        
        # 处理栈里剩余的
        while stack:
            j = stack.pop()
            h = heights[j]
            left = stack[-1] if stack else -1
            width = n - left - 1
            res = max(res, h * width)
        return res