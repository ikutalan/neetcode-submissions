class Solution:
    def isValid(self, s: str) -> bool:
        # if open, add to a stack
        # if close find if stack has the paired open bracket
        paired = {'(':')','[':']','{':'}'}
        stack = []
        if len(s) == 1:
            return False
        for char in s:
            if char in paired.keys():
                stack.append(char)
            else:
                if not stack:
                    return False
                n = stack.pop()
                if char != paired[n]:
                    return False
        if not stack:
            return True
        else: 
            return False