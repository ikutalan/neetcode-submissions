class Solution:
    def isValid(self, s: str) -> bool:
        # if open, add to a stack
        # if close find if stack has the paired open bracket
        paired = {'(':')','[':']','{':'}'}
        stack = []
        for char in s:
            if char in paired:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if char != paired[top]:
                    return False
        return not stack
        # edge case: all open, all close