class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        
        for idx, temp in enumerate(temperatures):
            if not stack:
                stack.append(idx)
                continue
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                res[j] = idx - j
            stack.append(idx)
        return res

                
