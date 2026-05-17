class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # use len(s1) to find if there's any len(s1) has the same char and char count
        # window size : len(s1)
        # what's in the window: the string need to be compare
        # when to move the window: the char in string does not have the same char and char count as s1
        if len(s1) > len(s2):
            return False

        l,r = 0, 0
        k = len(s1)
        c1 = Counter(s1)
        
        while r < len(s2):
            r = l+k
            if Counter(s2[l:r]) == c1:
                return True
            l += 1
        return False