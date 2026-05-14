class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # find max h * w
        # h = min (heights[i], heights[j]
        # w = j - i (j>i)

        i, j = 0, len(heights)-1
        res = 0
        while i < j:
            temp = min(heights[i], heights[j]) * (j - i)
            res = max(temp, res)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return res


        